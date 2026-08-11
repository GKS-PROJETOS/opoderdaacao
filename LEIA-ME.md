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

## Mudança pedida: 3 pacotes no lugar de 1

O site no ar tem **um único ingresso** (R$ 297 à vista / 6x R$ 49,50). A seção de
preço aqui foi refeita com **três pacotes lado a lado** — PADRÃO, PREMIUM e VIP —
numa grade de 3 colunas de 347px dentro dos 1090px da página. O card do meio é o
recomendado: contorno de 2px e o selo "MAIS ESCOLHIDO".

O preço e o botão ficam colados no rodapé de cada card (`margin-top:auto`), então
os três botões alinham na mesma linha mesmo com listas de tamanhos diferentes.
Abaixo de 900px os cards empilham em coluna única de 480px.

**Só o PADRÃO tem dado real** — é o ingresso e o link que existem hoje. Os itens,
os preços e os links de PREMIUM e VIP são provisórios e estão marcados no
`index.html` com o comentário `TROCAR`. Cada pacote precisa do seu próprio
checkout na Eduzz; hoje os três apontam para `E0DKDO4D91`.

Com isso a seção de preço passou de 752px para 856px de altura, e a página deixa
de bater com a original nessa seção — a tabela abaixo é de antes da mudança.

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
- Todos os botões de compra vão para `chk.eduzz.com/E0DKDO4D91?np=6`.
- A foto do mentor vinha em 2333×3499 para uma caixa de 353px; reduzi para 2x.
  Os originais estão intactos em `assets/real/`.
