# O Poder da Ação — recriação da landing page

Cópia de `eusougustavosampaio.com/opoderdaacao`. Abra o `index.html` direto no
navegador — não precisa de servidor.

```
opoderdaacao/
├── index.html
├── styles.css
└── assets/
    ├── img/    ← as 27 imagens usadas na página (nomes legíveis)
    └── real/   ← os mesmos arquivos como vieram do site, sem renomear
```

## Um problema encontrado no site original

O botão **"Fale com nosso time"** aponta para:

```
https://wa.me/556281084247
```

São 55 + 62 + **81084247** — 8 dígitos. Celular brasileiro tem 9, e o número
usado no site principal é `5562981084247` (com o 9 na frente). Do jeito que
está, o link provavelmente não abre a conversa.

Reproduzi exatamente como está no ar. Para corrigir, troque `556281084247` por
`5562981084247` no `index.html` (está marcado com comentário).

## Mudança pedida: 3 pacotes por quantidade, no lugar de 1

O site no ar tem **um único ingresso** (R$ 297 à vista / 6x R$ 49,50). Aqui a
seção de preço virou **três pacotes por quantidade de ingressos**, numa grade de
3 colunas de 347px dentro dos 1090px da página:

| | 1 INGRESSO | 2 INGRESSOS (destaque) | 5 INGRESSOS OU MAIS |
|---|---|---|---|
| De | — | ~~R$ 594,00~~ | ~~R$ 1.485,00~~ |
| Parcelado | 6x R$ 55,72 | 6x R$ 93,24 | 6x R$ 234,23 |
| À vista | R$ 297,00 | R$ 497,00 | R$ 1.248,50 |
| Selo | — | Economia de R$ 97 | Economia de R$ 236,50 |
| Checkout | `E0DKDO4D91` | `7WXG5GQY0A` | `39YNB33QWO` |

**O terceiro card era "10 INGRESSOS" (R$ 2.497 fixo) e virou "5 INGRESSOS OU
MAIS" em 17/08/2026**, a R$ 249,70 o ingresso. As contas do card saem daí, sobre
o piso de 5 pessoas:

```
De  = 5 × 297,00 = 1.485,00
Por = 5 × 249,70 = 1.248,50     economia de 236,50
```

O checkout próprio (`39YNB33QWO`) chegou no mesmo dia e o botão passou a apontar
para ele, com `data-checkout="pacote-5"`. **Ele fecha exatamente 5 unidades** —
a "Quantidade de ingressos" na tela da Eduzz é fixa, não dá para o comprador
subir para 6. Quem quer mais resolve na faixa **FAÇA SEU ORÇAMENTO**, logo
abaixo dos cards. Se um dia existir produto com quantidade variável a R$ 249,70,
é só trocar o `href`.

> O card chegou a ter, acima do botão, a linha *Mais de 5 ingressos? Faça seu
> orçamento* (`.card__nota`). Saiu no mesmo dia, a pedido: a faixa de orçamento
> vem logo depois e já diz isso, e a linha era a única coisa fora de padrão
> dentro dos três cards. Se voltar, tem que ficar **antes** do `<a>` — como
> `.card__price` tem `margin-top:auto`, o que vier depois dela encosta no rodapé
> do card, e com a nota abaixo do botão o botão deste card subia 29px e saía da
> linha dos outros dois.

> **Escada de preço invertida.** A casadinha sai a R$ 248,50 por pessoa e o
> pacote de 5 a R$ 249,70 — comprar 2 ingressos é R$ 1,20 mais barato por
> cabeça do que comprar 5. Por isso o card **não** anuncia "R$ 249,70 por
> ingresso" em lugar nenhum: só o total. Some se o pacote cair para R$ 1.198,50
> (R$ 239,70 cada) ou se a casadinha subir.

A parcela é **o valor que a Eduzz mostra na própria tela de checkout**, não o à
vista dividido por 6. O parcelamento em 6x tem juros (até 3,49% a.m.): R$ 297 à
vista dá 6x R$ 55,72 (R$ 334,32), e não 6x R$ 49,50; R$ 1.248,50 dá 6x
R$ 234,23, e não 6x R$ 208,08. A página chegou a mostrar a divisão
simples; foi corrigido em 14/08/2026, porque anunciar parcela menor que a
cobrada é propaganda enganosa. **Ao mexer em preço, ler os dois números direto
no checkout.**

Cada card tem três motivos em `.card__itens`, com o "check" desenhado no CSS
(sem imagem nova). Eles falam do **motivo de escolher aquele pacote**, não das
características do evento: o de 2 é "traga alguém com você e os dois pagam
menos", o de 5+ é "leve a sua equipe inteira na mesma turma".

O preço e o botão ficam colados no rodapé (`margin-top:auto`), então os três
botões alinham na mesma linha mesmo com um card tendo "de" riscado e selo de
economia e outro não. O do meio mantém o contorno de 2px, sem selo escrito.
Abaixo de 900px os cards empilham em coluna única de 480px.

## Faça seu orçamento

Abaixo dos três cards, a faixa **`.comercial`** atende quem não se encaixa nos
três cards — 3 ou 4 ingressos, nota no CNPJ, condição especial. **A quantidade e
o valor são resolvidos com o comercial no WhatsApp, não na página** — não há
calculadora nem preço por quantidade aqui.

Isso é de propósito: só existe preço oficial para 1, 2 e 5+ ingressos. Qualquer
valor mostrado para 3 ou 4 seria invenção, e num compromisso público de preço
isso não se faz. Quem decide é o comercial, na conversa.

Mesmo material dos cards (fundo `#1B1E2A`, borda dourada de 1px, raio 10px,
padding 30/24, h3 de 26px), ocupando a largura dos três, tudo centralizado:
título, chamada, dois motivos em 2 colunas e o botão "FAZER MEU ORÇAMENTO". O
botão é `inline-flex`, então quem o centraliza é o `text-align:center` do pai. A
lista reaproveita `.card__itens` só para herdar o check; `.comercial__itens` troca
as colunas. Abaixo de 900px a faixa vai para 480px e os motivos viram coluna
única.

O link vai para o WhatsApp com o número **de 9 dígitos** (`5562981084247`), não o
de 8 do botão "Fale com nosso time".

## Patrocínio

Último bloco da seção de preço, logo abaixo do orçamento: a faixa
**`.patrocinio`**, para a empresa que quer expor a marca no evento em vez de
comprar ingresso. Título, uma frase de apoio e o botão **QUERO PATROCINAR**,
que vai para o mesmo WhatsApp do comercial com mensagem própria.

É de propósito uma faixa **baixa** (155px no desktop contra 287px do orçamento),
com borda de aço `#A3BAC6` em vez de dourada e botão **verde de WhatsApp**: é um
convite, não um quarto pacote, e não pode disputar atenção com os três botões
dourados de compra logo acima. Texto à esquerda e botão à direita
(`justify-content: space-between`); abaixo de 900px empilha e centraliza, e
abaixo de 620px o botão vai a 100%/340px como os outros.

**Baixa é a altura, não a letra.** A faixa nasceu com título de 20px, apoio de
14px e botão de 236×48 — menor que tudo em volta, o que a fazia parecer um
rodapé. Em 17/08/2026 passou para a escala padrão da seção: h3 de 26px/36,4px e
apoio de 15px/21px (igual ao `.comercial` e aos cards), botão no tamanho normal
do `.btn--wa` (317×54, o mesmo do rodapé), e no mobile 22px/14px como o
orçamento. O que segura a altura é o padding de 22px e o texto em uma linha só
de conteúdo, não a tipografia miúda.

Não fala de valor de cota — quem define é o comercial, mesma regra do orçamento.
Se o patrocínio ganhar um contato próprio (e-mail ou outro número), trocar só o
`href` desse botão, marcado com comentário no HTML.

## Checkouts

| Card | Produto na Eduzz | Link |
|---|---|---|
| 1 ingresso | Ingresso O Poder da Ação — Lote 1 | `chk.eduzz.com/E0DKDO4D91?np=6` |
| 2 ingressos | Ingresso Duplo | `chk.eduzz.com/7WXG5GQY0A?np=6` |
| 5 ingressos ou mais | Lote 5 (5 unidades, R$ 1.248,50) | `chk.eduzz.com/39YNB33QWO?np=6` |

Os dois primeiros chegaram em 14/08/2026 e o terceiro em 17/08/2026; antes disso
todos apontavam para o `E0DKDO4D91` do de 1 ingresso. O `G96RVR8YW1` ("Ingresso
10 pessoas — Lote 10 Ingressos", R$ 2.497 fixo) **saiu da página** em 17/08/2026,
quando o card de 10 virou 5+ — continua existindo na Eduzz, mas não é usado. Os
`<a>` continuam marcados com `data-checkout="casadinha"` e
`data-checkout="pacote-5"` para achar rápido.

O nome do produto na Eduzz não é igual ao título do card ("Ingresso Duplo" ×
"2 INGRESSOS"). Quem clica vê o nome da Eduzz no checkout.

Com isso a seção de preço passou de 752px para **1338px** de altura no desktop
(1176px antes da faixa de patrocínio), e a página deixa de bater com a original
nessa seção — a tabela abaixo é de antes da mudança.

## Ícone da aba (favicon)

Até 17/08/2026 a página não tinha ícone nenhum — a aba do navegador mostrava o
globo cinza padrão. Agora usa o **alvo com a flecha**, o mesmo motivo da capa do
livro, em `assets/icon/`:

| Arquivo | Para quê |
|---|---|
| `favicon.svg` | a fonte, e o que o navegador moderno usa (escala sem borrar) |
| `favicon-32.png` | reserva de quem não lê SVG |
| `favicon.ico` | 16/32/48px, reserva de navegador antigo |
| `apple-touch-icon.png` | 180px, atalho na tela inicial do iPhone |

O desenho é geometria pura, sem imagem externa: cinco círculos concêntricos
(r 31 / 24 / 17 / 10 / 4,5 num `viewBox` de 64) alternando vermelho `#E02A1B` e
branco, e a flecha desenhada na vertical e girada 45° para cravar na mosca vindo
de cima à direita. Ela é **um polígono só** (penas + haste + ponta), em dourado
`#E49525` com contorno `#12141C`: em peças separadas o contorno de cada uma
aparece por dentro e a 16px a flecha vira um borrão escuro.

O `apple-touch-icon` é o único com fundo (`#12141C`, o `--bg` do site), porque o
iPhone não respeita transparência no atalho. **Mexeu no SVG, gerar os PNG de
novo** — eles não saem do SVG sozinhos; foram desenhados com a mesma geometria
em Pillow, com 16× de supersampling e redução em LANCZOS.

## Botões

**Alinhamento do CTA do hero.** No original a caixa de data/hora/local (484px) e
o botão (385px) dividem o mesmo eixo central: caixa em `x=86`, botão em `x=135`,
os dois com centro em **328**. Ou seja, o botão é recuado em 49,5px, não encostado
à esquerda. `.hero__text .btn--cta { margin-left: calc((484px - 385px) / 2) }`
reproduz isso sem wrapper novo no HTML, e abaixo de 620px o recuo volta a zero —
lá a caixa ocupa 100% e quem centraliza é o `text-align` do `.hero__text`.

Os outros dois CTAs não levam recuo: no original o da faixa da citação fica à
direita do texto e o de "esse evento é para você" já é centrado na página.

O original usa cor chapada com peso 400, o que deixa o botão apagado. Aqui todos
os `.btn` levam peso **700**, degradê vertical, luz interna na aresta de cima,
halo colorido embaixo e uma faixa de brilho que atravessa no hover (`::after`),
mais `translateY(-2px)` ao passar o mouse e afundar de 1px no clique. O
`prefers-reduced-motion` desliga o brilho e o levantar. Isso exigiu carregar
**Open Sans 700** no `<link>` das fontes — sem isso o navegador fabricava um
negrito falso.

## Telefone

A maior parte do tráfego vem do celular, e abaixo de **620px** a organização do
topo passa a ser a mesma do original:

- a foto do Gustavo sai do fluxo (`.hero__figure` escondida) e vira **fundo** do
  `.hero__intro`, uma caixa de 463px de altura com degradê dissolvendo no fundo;
- `O PODER DA AÇÃO` (31px) e a chamada (24px/33.6px) ficam **sobrepostos na base
  da foto**, centralizados. O `.hero__intro` usa 4px de lateral em vez dos 20px
  da section: é o que o original faz, e é o que mantém a chamada em duas linhas;
- o texto de apoio, a caixa de data/hora/local e o botão passam para **baixo da
  foto**, já no fundo escuro.

A escala de tipografia das seções também desceu para perto da do original
(descrições em 13px, itens de "esse evento é para você" em 14px, títulos de "o
que vai levar" em 18px, respostas do FAQ em 14px). Onde o original usa 12px eu
subi para 13px — 12px é pequeno demais para ler no telefone.

Resultado: a página no telefone caiu de **12267px para 10366px**. O original tem
8473px, e a diferença que sobra é quase toda a seção de preço, que aqui tem três
pacotes e uma faixa em vez de um card só.

## Como foi feito

Os valores saíram do CSS aplicado na página no ar: cores, fontes, tamanhos,
espaçamentos, imagens e links. A original é feita na GreatPages, que empilha
blocos sobre um canvas de 980px e posiciona cada elemento de forma absoluta.
Aqui a mesma composição foi remontada com grid/flex, o que mantém o resultado
igual no desktop e faz o layout continuar válido em telas menores.

Conferência de altura por seção (viewport de 1357px de conteúdo):

| Seção | Original | Cópia |
|---|---|---|
| hero | 736 | 736 |
| 6 áreas | 507 | 496 |
| faixa da citação | 330 | 330 |
| esse evento é pra você | 713 | 709 |
| mentor | 877 | 892 |
| o que vai levar | 1379 | 1399 |
| preço | 784 | 752 |
| FAQ | 485 | 486 |
| ajuda | 203 | 203 |
| rodapé | 49 | 56 |
| **página inteira** | **6063** | **6061** |

## Molduras, fundos e contornos

Detalhes fáceis de passar batido numa leitura só de tipografia, todos conferidos
no CSS aplicado do site:

| Elemento | Tratamento |
|---|---|
| Caixa de data / hora / local | fundo `#12141C`, borda 1px `#D96A1F`, raio 12px |
| Ícones de "esse evento é para você" | caixa 110×104, borda 1px **vermelha**, raio 20px |
| Foto do mentor | raio 14px, com moldura dourada 2px atrás, deslocada 8px à direita e 15px abaixo |
| Os 3 números | card `#1D2232`, borda 1px `#E49525`, raio 7px |
| Linhas de "o que vai levar" | card `#1D2232`, raio 25px, imagem interna com raio 15px |
| Perguntas do FAQ | card `#1D2232`, raio 8px + `overflow:hidden`, ícone de 24px à direita |
| Caixa do preço | fundo `#12141C`, borda 1px `#A3BAC6` (cinza-azulado, não dourada) |
| Base da foto do hero | degradê de 150px dissolvendo a foto no fundo |

## Detalhes

- Fontes: Poppins (texto) e Open Sans (botões), como no original.
- Cores: fundo `#12141C`, faixa `#212836`, card de preço `#1B1E2A` com borda
  `#E49525`, botões `#DD8810`, WhatsApp `#0EA94A`, texto de apoio `#91999D`.
- **FAQ**: pergunta e resposta formam **um card só** — o raio de 8px e o
  `overflow:hidden` ficam no item, então o painel aberto continua o mesmo bloco
  escuro do cabeçalho. Resposta em `#91999D` (`--g-color-muted` do tema) sobre
  `#1D2232` (`--g-color-secondary`), padding `0 12px 12px`, fonte 15,48px.
  O "+" gira 45° e vira "×" ao abrir, e o painel desliza em 280ms.
  Sem JavaScript as respostas ficam abertas e legíveis — é o script que as
  recolhe, então a página nunca fica com conteúdo inacessível.
- Os três CTAs de fora da seção de preço (hero, faixa da citação, "esse evento é
  para você") vão para o checkout de **1 ingresso** (`E0DKDO4D91`); os botões dos
  cards vão cada um para o seu, na tabela acima.
- A foto do mentor vinha em 2333×3499 para uma caixa de 353px; reduzi para 2x.
  Os originais estão intactos em `assets/real/`.


## Deploy no Cloudflare

Este projeto agora e publicado em eusougustavosampaio.com/opoderdaacao via uma rota do Cloudflare Workers apontando para este worker. O build empacota os arquivos dentro de uma subpasta opoderdaacao/ para casar com o prefixo da rota.
