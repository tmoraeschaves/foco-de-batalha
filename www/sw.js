const CACHE = 'foco-batalha-v10';
const ASSETS = [
  './',
  './index.html',
  './batalhas.json',
  './manifest.json',
  './icons/icon.svg'
];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE).then(cache => cache.addAll(ASSETS))
  );
  self.skipWaiting();
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request).then(cached => {
      if (cached) return cached;
      return fetch(e.request).then(res => {
        if (res.ok) {
          const clone = res.clone();
          caches.open(CACHE).then(c => c.put(e.request, clone));
        }
        return res;
      }).catch(() => {
        // Fallback: ícones PNG ausentes → retorna SVG
        if (e.request.url.endsWith('.png') && e.request.url.includes('/icons/')) {
          return caches.match('./icons/icon.svg');
        }
        return cached;
      });
    })
  );
});
