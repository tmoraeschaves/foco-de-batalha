# FOCO DE BATALHA — CLAUDE.md

## Visão Geral
RPG educacional mobile chamado "FOCO DE BATALHA — Academia de Pupilos da Aura".
Single-file PWA + Capacitor Android. Sem backend. Tudo em localStorage.

## Estrutura do Projeto

```text
D:\GITHUB\FOCO_DE_BATALHA\
├── www/
│   ├── index.html      ← Jogo completo (~350 KB, todo CSS/JS embutido)
│   ├── batalhas.json   ← 1.419 sementes de conhecimento (PT/EN/ES, ~1.2 MB)
│   ├── manifest.json   ← PWA manifest (lang pt-BR, ícones separados por purpose)
│   ├── sw.js           ← Service Worker v8 (cache offline)
│   ├── img/            ← Arte do jogo: guerreiro/mago/paladino/lanceiro/assassino/druida/boss_goblin/pupilo/abertura/capa.png
│   └── icons/          ← icon-192.png, icon-512.png, icon.svg
├── store-assets/       ← feature-graphic.png (1024×500)
├── android/            ← Projeto Android gerado pelo Capacitor
├── node_modules/
├── package.json        ← Capacitor 6 + plugins
├── capacitor.config.json
├── privacy.html        ← Política de Privacidade (LGPD) — hospedado no GitHub Pages
├── support.html        ← Suporte + página de anunciantes
├── store-listing.md    ← Textos prontos para Play Store (PT/EN/ES)
└── feature_graphic.html← HTML alternativo do Feature Graphic
```

## Arquivos Principais

| Arquivo | Descrição |
| ------- | --------- |
| `www/index.html` | Todo o jogo: CSS + HTML + JS em um único arquivo (~6400 linhas) |
| `www/batalhas.json` | Sementes de conhecimento: nivel 1/2/3, semente, pergunta, opcoes, correta + EN/ES |
| `www/img/` | Arte das 6 classes, boss, personagem pupilo, tela de abertura |
| `android/` | Projeto Android Studio gerado por `npx cap sync` |

## Estado do Jogo (maio 2026)

### Funcionalidades completas

- Sistema de batalha com HP (jogador + inimigo), 30+ inimigos, boss semanal (sábado/domingo)
- 6 classes com artes: Guerreiro, Mago, Paladino, Lanceiro, Assassino, Druida
- Lightbox de classe: toque no card abre imagem full com botão confirmar
- 150 níveis com progressão Fibonacci
- 9 ranques: Pupilo → Primário
- Inventário com tiers: Básico (5 slots) / Prata (10) / Ouro (20) / Lendário (30)
- Loja, Battle Pass (2000💰), daily streak, 20+ conquistas
- i18n PT-BR / EN / ES (LANG = constante 'pt-br' em v1.0)
- PWA offline-first + cloud save (Play Games)
- Backup/restore via código Base64
- Gift codes com expiração
- Botão Voltar Android tratado (Capacitor App plugin)
- Filtro de sementes por nível: LV1-20 só nivel 1, LV21-100 nivel 1+2, LV101+ todas
- Modo Sobrevivência preserva estado do jogo principal ao entrar/sair

### Arte integrada

Imagens em `www/img/` (geradas por Gemini + ChatGPT):

- Cards de classe: `object-position` individual por personagem (definido em CSS)
- Viewer de classe (lightbox): posicionamento próprio em `#cls-viewer[data-cls="..."]`
- Menu: avatar circular da classe ativa; arte do boss nos finais de semana

### Preços atuais (maio 2026)

| Item | Preço |
| --- | --- |
| Battle Pass | 2000💰 |
| Tier Prata | 1000💰 |
| Tier Ouro | 2000💰 |
| Tier Lendário | 3000💰 |
| Poção de Vida | 50💰 |
| Poção de Saltos | 100💰 |
| Talismã de Ouro | 150💰 (1ª vez) / 300💰 |
| Itens premium | 150→200→250→300→350→400→450💰 |
| Slot avulso | 150💰 |
| Loja Rotativa | 300💰 base / 150💰 (50% off) |
| Moedas iniciais | 100💰 (novo jogador) |

### Gift Codes ativos

- `FOCO2026` — Pack de Boas-Vindas (expira 31/12/2026)
- `AURA2026` — Pack da Aura (expira 30/06/2026)

### Privacidade — URL pública

`https://tmoraeschaves.github.io/foco-de-batalha/privacy.html`

### Pendente para Play Store (v1.0)

- [x] Feature Graphic 1024×500 PNG — em `store-assets/feature-graphic.png`
- [x] `npm install && npx cap sync` — feito
- [x] Sincronizar GitHub — feito (branch main sincronizado)
- [x] Adaptive icon — gerado em todas as densidades (mdpi→xxxhdpi)
- [x] Build `.aab` assinado — gerado em `android\app\build\outputs\bundle\release\app-release.aab`
- [ ] Instalar APK de teste no dispositivo (Android Studio → Run → Run 'app')
- [ ] Screenshots mín. 2 (16:9) no emulador
- [ ] Classificação etária IARC no Play Console
- [ ] Upload do .aab no Play Console

### Dívida técnica conhecida

- **batalhas.json**: ~813 perguntas EN não traduzidas (cópia do PT); ~838 ES
- **batalhas.json**: Algumas traduções parciais (mistura PT+EN nas frases)
- **G.battle.playerHP** vs **G.vidas**: dois rastreadores de HP paralelos; `G.vidas` é o real. `G.battle.playerHP` começa no máximo da classe (ex: 12) — sem bug pois toda checagem de derrota usa `G.vidas`

### Pós-lançamento (v1.1)

- AdMob real (`@capacitor-community/admob`)
- Google Play Billing (IAP real)
- Firebase Analytics
- FCM (notificações push remotas)
- Tradução completa das 813+ perguntas PT→EN/ES no batalhas.json

## Modelo de Negócio

- Anúncios recompensados (voluntários, troca por itens)
- IAP — loja de moedas (placeholder funcional)
- Battle Pass (2000 moedas/temporada)
- B2B — Sementes Patrocinadas (empresas pagam para inserir conteúdo)

## Comandos

```bash
npm install
npx cap sync
npx cap open android   # abre Android Studio para build .aab
```

## GitHub

- Repositório: <https://github.com/tmoraeschaves/foco-de-batalha>
- GitHub Pages: <https://tmoraeschaves.github.io/foco-de-batalha/>
