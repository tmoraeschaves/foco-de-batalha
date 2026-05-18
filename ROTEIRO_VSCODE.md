# 🗡️ ROTEIRO COMPLETO — FOCO DE BATALHA
## Para colar no chat do VS Code (GitHub Copilot / Cursor / Claude Dev)

---

## MISSÃO GERAL

Você está construindo o jogo mobile **"FOCO DE BATALHA — Academia de Pupilos da Aura"**.
É um jogo de foco cognitivo com temática medieval RPG.
Todos os arquivos ficam em uma única pasta do projeto.

---

## ARQUIVOS DO PROJETO

```
/projeto
  index.html          ← App principal (já existe, vai ser substituído)
  batalhas.json       ← Banco de 1.396 sementes (já existe)
  README.md           ← Documentação (criar)
```

---

## PROMPT 1 — SUBSTITUIR O INDEX.HTML COMPLETO

Cole este prompt no chat:

---

**PROMPT:**

Substitua o conteúdo de `index.html` pelo jogo completo abaixo.
O arquivo `batalhas.json` já existe na mesma pasta e contém 1.396 sementes.
O jogo deve carregar as sementes via `fetch('./batalhas.json')` na inicialização.

### ESPECIFICAÇÕES COMPLETAS:

**VISUAL:**
- Tema medieval RPG dark, fontes Cinzel + Crimson Pro (Google Fonts)
- Paleta: ouro (#c9a84c), pedra (#0c0905), pergaminho (#f0e0c0), arcano (#6b2fa0)
- Canvas de partículas douradas flutuantes no fundo
- Animações suaves em todas as transições

**TIMERS (atualizar dos valores atuais):**
- SEMENTE: 25 segundos de leitura (era 10+nível)
- NÉVOA/DISTRAÇÃO: 30 segundos (já correto)
- RESPOSTA: 25 segundos (era 12)

**TELAS NECESSÁRIAS (screens):**
1. `#sw` — Welcome/Intro com história e escolha de classe
2. `#sg` — Game (semente → névoa → questão)
3. `#sr` — Ranking/Mural dos Heróis
4. `#sh` — Loja de itens
5. `#ss` — Tela de salvar/configurações
6. `#sn` — Tela de novo nível (capítulo)

**CLASSES RPG (6 opções, layout 2x3):**
- ⚔️ GUERREIRO — Resiliência bruta. Começa com +1 vida extra
- 🔮 MAGO — Visão arcana. Vê a categoria da semente com antecedência
- 🛡️ PALADINO — Foco sagrado. Timer da névoa 5s mais curto
- 🏹 LANCEIRO — Precisão mortal. +2 pontos por acerto rápido (<10s)
- 🗡️ ASSASSINO — Sombras e furtividade. Começa com +2 pulos
- 🌿 DRUIDA — Sabedoria natural. Maior chance de recompensa dupla

**SISTEMA DE SEMENTES:**
- Carrega `batalhas.json` via fetch
- Campo `nivel` (1,2,3) já existe no JSON
- Campo `semente` = texto a exibir
- Campo `pergunta` = pergunta após névoa
- Campo `opcoes` = array com 4 strings
- Campo `correta` = índice 0-3

**FLUXO DE CADA RODADA:**
1. Tela SEMENTE: exibe texto + categoria + timer 25s regressivo
2. Tela NÉVOA: animação de distração + frases da Aura + timer 30s
   → Aqui entrarão os anúncios AdMob no futuro (apenas placeholder por ora)
3. Tela QUESTÃO: 4 botões de resposta + timer 25s + botão "⚡ USAR PULO"

**HUD (cabeçalho fixo):**
- ❤️ vidas (máx 5)
- ⚡ pulos (máx 5) 
- 🔥 streak
- Rank atual
- Nível atual
- Barra de progresso para próximo nível

**SISTEMA DE NÍVEIS:**
- Títulos de capítulo inspiradores ao subir de nível (ex: "⚔️ CAPÍTULO II — O DESPERTAR DA CHAMA")
- Nível = Math.floor(acertos / threshold) + 1
- Threshold por faixa:
  - Níveis 1-10: 5 acertos por nível
  - Níveis 11-25: 8 acertos por nível
  - Níveis 26-50: 13 acertos por nível
  - Níveis 51+: 21 acertos por nível
  (números primos: 5, 8, 13, 21 — sequência Fibonacci)

**TÍTULOS DE CAPÍTULO (ao subir de nível):**
```javascript
const CHAPTER_TITLES = [
  "O CHAMADO DAS SOMBRAS",
  "O DESPERTAR DA CHAMA",
  "A FORJA DO ESPÍRITO",
  "O PRIMEIRO SANGUE",
  "ENTRE LUZ E TREVAS",
  "A VOZ DO ABISMO",
  "O PESO DA COROA",
  "ALÉM DO HORIZONTE",
  "A PROFECIA SE CUMPRE",
  "O MESTRE REVELA O CAMINHO",
  "AS SOMBRAS RECUAM",
  "O GOVERNANTE EMERGE",
  "A BATALHA FINAL",
  "O SILÊNCIO APÓS A TEMPESTADE",
  "A LENDA COMEÇA"
];
```

**SISTEMA DE RANQUES:**
```javascript
const RANKS = [
  {min:0,    name:"PUPILO",      icon:"🌱", cor:"#6a8a4a"},
  {min:25,   name:"ESCUDEIRO",   icon:"🗡️", cor:"#8a7a4a"},
  {min:60,   name:"INICIADO",    icon:"⚔️", cor:"#c9a84c"},
  {min:120,  name:"GUARDIÃO",    icon:"🛡️", cor:"#5a8ab0"},
  {min:220,  name:"CAMPEÃO",     icon:"🏆", cor:"#9a5ac9"},
  {min:380,  name:"MESTRE",      icon:"🔮", cor:"#c95a5a"},
  {min:600,  name:"ARCONTE",     icon:"👁️", cor:"#c9784c"},
  {min:900,  name:"LENDÁRIO",    icon:"⭐", cor:"#f0d080"},
  {min:1300, name:"PRIMÁRIO",    icon:"👑", cor:"#ffffff"},
];
```

**SISTEMA DE PRÊMIOS (Altar da Aura):**
- A cada nível atingido → tela de capítulo → depois escolha de prêmio
- Prêmios se alternam: ❤️ Vida → ⚡ Pulo → ❤️ Vida → ⚡ Pulo...
- LIMITE de estoque: vidas máx 5, pulos máx 5
- Se ambos cheios → aparece opção "🛒 VISITAR A LOJA"
- Se não tem itens ao errar → aparece opção "📺 ASSISTIR ANÚNCIO" (placeholder)

**TELA DA LOJA (#sh):**
```
╔══════════════════════════════╗
║    ⚔ FORJA DO AVENTUREIRO ⚔  ║
╠══════════════════════════════╣
║  ❤️ VIDA EXTRA     [GANHAR]  ║
║     Estoque: X/5             ║
║  ⚡ PULO EXTRA     [GANHAR]  ║
║     Estoque: X/5             ║
╠══════════════════════════════╣
║  💎 PACOTES PREMIUM          ║
║  [5 Vidas]  [5 Pulos]        ║
║  [Proteção de streak]        ║
╚══════════════════════════════╝
```
- Itens ganhos: limitados pelo estoque máx 5
- Itens "comprados" (premium): sem limite de estoque (futura integração Play Billing)
- Botão para assistir anúncio em troca de 1 item (placeholder)

**TELA SALVAR/SAIR (#ss):**
- Botão SALVAR: salva estado no localStorage
- Botão SAIR: confirma e volta para tela welcome
- Exibe: pontuação atual, nível, rank, streak

**SISTEMA DE IDIOMAS (i18n):**
```javascript
const LANG = {
  'pt-br': {
    btn_start: "ENTRAR NA MASMORRA",
    btn_save: "SALVAR PROGRESSO",
    btn_exit: "SAIR",
    phase_seed: "✦ ESTUDE A SEMENTE ✦",
    phase_fog: "✦ A NÉVOA CHEGA... ✦",
    phase_answer: "✦ RESPONDE AGORA ✦",
    // ... etc
  },
  'en': {
    btn_start: "ENTER THE DUNGEON",
    btn_save: "SAVE PROGRESS",
    btn_exit: "EXIT",
    phase_seed: "✦ STUDY THE SEED ✦",
    phase_fog: "✦ THE FOG ARRIVES... ✦",
    phase_answer: "✦ ANSWER NOW ✦",
  },
  'es': {
    btn_start: "ENTRAR AL CALABOZO",
    btn_save: "GUARDAR PROGRESO",
    btn_exit: "SALIR",
    phase_seed: "✦ ESTUDIA LA SEMILLA ✦",
    phase_fog: "✦ LA NIEBLA LLEGA... ✦",
    phase_answer: "✦ RESPONDE AHORA ✦",
  }
};
```
- Seletor de idioma na tela welcome (🇧🇷 🇺🇸 🇪🇸)
- Salva preferência no localStorage

**MODO HISTÓRIA — NARRATIVA DA AURA:**
```
Tela de abertura antes da tela Welcome:
"Das sombras que pairam sobre as mentes fracas, emerge um mal antigo.
Dizem as profecias que apenas aquele com domínio sobre si mesmo
está fadado a governar estas terras vastas.

Tu que chegaste até aqui... serás esse governante?

A Aura observa. O caminho sem retorno começa agora."
```

**FRASES DA AURA durante a névoa:**
```javascript
const AURA_TAUNTS = [
  "A névoa tenta apagar a tua mente...",
  "Mantém a chama do foco acesa, Pupilo.",
  "O barulho do mundo testa a tua resistência.",
  "Concentra-te. A resposta ainda vive em ti.",
  "A distração é o inimigo. Tu és mais forte.",
  "Fecha os olhos da alma. Apenas o foco importa.",
  "As sombras sussurram mentiras. Recorda a semente.",
  "O governante das terras vastas não vacila.",
  "Tua mente é fortaleza. Não a abandones.",
  "A profecia diz: apenas o focado prevalece.",
];
```

**FRASES DE ACERTO:**
```javascript
const OK_MSG = [
  "A tua chama de foco arde com força. Avança, Iniciado.",
  "Excelente retenção. A névoa não venceu tua mente.",
  "Assim se forja um mestre da atenção.",
  "O ruído passou. A memória permaneceu. Perfeito.",
  "Tua resiliência é diamante. Continua.",
  "As sombras recuam. Tua mente é clara.",
  "YHWH forjou em ti uma mente de aço. Usa-a.",
];
```

**FRASES DE ERRO:**
```javascript
const KO_MSG = [
  "A distração venceu desta vez. Mas tu persistes.",
  "A névoa apagou tua memória. Não há vergonha — treina mais.",
  "Recalibra tua mente e retorna mais forte, Pupilo.",
  "O erro não existe — é apenas um ponto de quebra de resiliência.",
  "Até os mestres caem. O que os define é o retorno.",
  "A sombra tocou tua mente. Expulsa-a com foco.",
];
```

**NAVIGATION:**
- Bottom nav com 4 tabs após iniciar:
  - ⚔️ BATALHA
  - 📜 RANKING  
  - 🛒 LOJA
  - ⚙️ MENU (salvar/sair/idioma)

**RANKING:**
- Salvo em localStorage (`pda-rk`)
- Campos: nick, cls, ico, pts, streak, rank, lv, data
- Top 50 jogadores
- Mostra medalhas 👑🥈🥉 para top 3
- Filtro por: Todos / Minha Classe

**SAVE/LOAD:**
```javascript
// Salvar estado completo
function saveGame() {
  const state = {
    nick, cls, ico, vidas, pulos, pts, streak, lv, cy,
    idx, lang, timestamp: Date.now()
  };
  localStorage.setItem('pda-save', JSON.stringify(state));
}

// Carregar ao iniciar
function loadGame() {
  const saved = localStorage.getItem('pda-save');
  if (saved) {
    // Mostra opção "Continuar" na tela welcome
  }
}
```

**BOTÃO SALVAR & SAIR:**
- No HUD: botão "💾" pequeno no canto
- Ao clicar: overlay de confirmação com opções SALVAR / SAIR / CANCELAR
- Salvar: persiste estado, mostra "✓ Progresso salvo"
- Sair: volta para tela Welcome sem perder save

**ESTRUTURA HTML FINAL:**
```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <!-- meta, fonts, title -->
</head>
<body>
  <canvas id="bg-canvas"></canvas>
  
  <!-- INTRO HISTÓRIA (aparece 1x) -->
  <div id="intro-story" class="screen active">...</div>
  
  <!-- HUD fixo (oculto até começar) -->
  <div id="hud">...</div>
  
  <!-- TELAS -->
  <div id="sw" class="screen"><!-- Welcome --></div>
  <div id="sg" class="screen"><!-- Game --></div>
  <div id="sr" class="screen"><!-- Ranking --></div>
  <div id="sh" class="screen"><!-- Loja --></div>
  <div id="ss" class="screen"><!-- Save/Settings --></div>
  
  <!-- OVERLAYS -->
  <div id="ov-result"><!-- Acerto/Erro --></div>
  <div id="ov-level"><!-- Novo nível --></div>
  <div id="ov-save"><!-- Salvar/Sair --></div>
  
  <!-- BOTTOM NAV -->
  <div id="bottom-nav">...</div>
  
  <script>
    // 1. Constantes e dados
    // 2. Estado global (G)
    // 3. i18n
    // 4. Canvas background
    // 5. Tela de intro/história
    // 6. Welcome (classes, nick, idioma)
    // 7. Game loop (nextRound → semente → névoa → questão → resultado)
    // 8. Sistema de níveis e capítulos
    // 9. Sistema de recompensas e loja
    // 10. Ranking
    // 11. Save/Load
    // 12. Navigation
  </script>
</body>
</html>
```

---

## PROMPT 2 — AJUSTES APÓS VER O RESULTADO

Após implementar o PROMPT 1, envie:

"Revise estes pontos:
1. O timer da semente deve ser exatamente 25s (não variável)
2. O timer da resposta deve ser exatamente 25s
3. A tela de novo nível deve aparecer com animação antes de voltar ao jogo
4. O botão SALVAR & SAIR deve estar sempre visível no HUD
5. Confirme que fetch('./batalhas.json') está funcionando e o jogo não usa SEEDS inline"

---

## PROMPT 3 — POLISH E ENGAJAMENTO

"Adicione estes elementos de engajamento:
1. Som visual (flash de cor) ao acertar/errar (sem áudio real)
2. Contador de dias seguidos jogando (daily streak) salvo no localStorage
3. Mensagem especial ao atingir 7 dias seguidos
4. Animação de partículas douradas ao subir de nível
5. Vibração (navigator.vibrate) ao acertar (50ms) e ao errar (200ms)
6. Meta tag theme-color para deixar a barra do Android dourada"

---

## PROMPT 4 — TELA DE INTRO/HISTÓRIA

"Crie uma tela de intro que aparece apenas uma vez (primeira vez que abre o app).
Usa animação de texto aparecendo linha por linha.
Texto da profecia:
'Das sombras que pairam sobre as mentes fracas...'
'...emerge um mal antigo que corrói a clareza.'
'As profecias falam de um ser com domínio absoluto sobre si mesmo.'
'Alguém fadado a governar as terras vastas.'
'Alguém capaz de ver através da névoa.'
'Esse alguém... pode ser você.'
[Botão: INICIAR JORNADA]
Salva no localStorage que o usuário já viu a intro."

---

## PROMPT 5 — INTEGRAÇÃO PWA

"Configure o jogo como PWA (Progressive Web App):
1. Crie manifest.json com:
   - name: 'Foco de Batalha'
   - short_name: 'FocoBatalha'
   - theme_color: '#c9a84c'
   - background_color: '#0c0905'
   - display: 'standalone'
   - orientation: 'portrait'
2. Adicione meta tags PWA no head do index.html
3. Crie service-worker.js básico que faz cache do batalhas.json
4. Registre o service worker no index.html"

---

## ESTRUTURA DE PASTAS FINAL

```
/foco-de-batalha/
  index.html          ← App principal
  batalhas.json       ← 1.396 sementes
  manifest.json       ← PWA manifest
  service-worker.js   ← Cache offline
  README.md           ← Documentação
  /icons/             ← Ícones do app (criar SVG simples)
    icon-192.png
    icon-512.png
```

---

## NOTAS IMPORTANTES PARA O DESENVOLVEDOR

1. **Sementes:** O `batalhas.json` usa campos `nivel`, `semente`, `pergunta`, `opcoes`, `correta`
2. **Timers:** 25s leitura / 30s névoa / 25s resposta — FIXOS, não variáveis
3. **Níveis primos:** thresholds 5, 8, 13, 21 (Fibonacci como primos de progressão)
4. **Monetização futura:** A névoa de 30s é onde entrará AdMob — deixar comentário no código
5. **Idiomas:** Estrutura i18n deve estar pronta mesmo que só PT-BR funcione no MVP
6. **Save:** Sempre salvar ao sair da tela de jogo (pausa, minimizar, etc.)
7. **Ranque:** Calcular e atualizar a cada acerto, não só ao fim
8. **Classe Guerreiro:** +1 vida inicial (começa com 2 vidas)
9. **Classe Assassino:** +2 pulos iniciais (começa com 3 pulos)
10. **Classe Paladino:** Névoa dura 25s em vez de 30s
11. **Classe Lanceiro:** +2 pts se responde em menos de 10s
12. **Classe Mago:** Mostra categoria da semente com 3s de antecedência
13. **Classe Druida:** Recompensa a cada 4 acertos em vez de 5 (nível 1-10)

