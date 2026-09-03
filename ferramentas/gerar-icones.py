# Gera os arquivos de icone de assets/icon/ a partir do alvo com a flecha.
#
#   python ferramentas/gerar-icones.py
#
# A fonte do desenho e assets/icon/favicon.svg. Como ele usa gradiente e filtro
# de sombra, rasterizar por geometria em Pillow (como era o icone antigo) nao
# reproduz mais o desenho - entao a rasterizacao vem de um PNG grande exportado
# do proprio SVG, guardado aqui em ferramentas/alvo-flecha-3000px.png, e daqui
# para baixo e so reducao em LANCZOS.
#
# Mexeu no SVG: exportar o PNG de 3000px de novo (abrir o SVG no navegador em
# 3000px e salvar), substituir o arquivo aqui e rodar este script.
#
# Por que cada tamanho tem tratamento proprio: o desenho tem SETE aneis. A 180px
# e a 512px isso e detalhe bonito; a 32px os aneis brancos ja lavam para rosa, e
# a 16px viram um borrao. Por isso os tamanhos pequenos levam saturacao (e o de
# 16px tambem um unsharp) - sem isso a aba do navegador mostra uma bola rosa.
# Nao trocar por um desenho simplificado sem falar: o pedido foi usar ESTE alvo.

import struct
from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
FONTE = AQUI / "alvo-flecha-3000px.png"
DESTINO = RAIZ / "assets" / "icon"
BG = (0x12, 0x14, 0x1C, 255)   # --bg do site: o unico fundo usado nos icones

# --- mestre quadrado, o desenho centrado com 2% de folga -------------------
im = Image.open(FONTE).convert("RGBA")
x0, y0, x1, y1 = im.getchannel("A").getbbox()
cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
lado = int(max(x1 - x0, y1 - y0) * 1.02)
MESTRE = Image.new("RGBA", (lado, lado), (0, 0, 0, 0))
MESTRE.paste(im, (int(lado / 2 - cx), int(lado / 2 - cy)))


def icone(px, fundo=None, ocupa=1.0, cor=1.0, nitidez=0):
    """Um icone quadrado de px. 'ocupa' e a fracao do lado que o desenho toma
    (so faz sentido com fundo), 'cor' e o ganho de saturacao e 'nitidez' o
    percentual de unsharp - os dois servem aos tamanhos pequenos."""
    d = int(px * ocupa)
    arte = MESTRE.resize((d, d), Image.LANCZOS)
    if cor != 1.0:
        arte = ImageEnhance.Color(arte).enhance(cor)
    if nitidez:
        arte = arte.filter(ImageFilter.UnsharpMask(radius=1, percent=nitidez, threshold=0))
    base = Image.new("RGBA", (px, px), fundo or (0, 0, 0, 0))
    base.alpha_composite(arte, ((px - d) // 2, (px - d) // 2))
    return base


def salvar_ico(caminho, imagens):
    """Escreve um .ico com um PNG por tamanho. Pillow, no save de ICO, reduz ele
    mesmo a partir de uma imagem so - e ai o de 16px sai sem o tratamento que
    ele precisa. O container e simples, entao vale montar na mao."""
    from io import BytesIO
    blocos = []
    for img in imagens:
        buf = BytesIO()
        img.save(buf, format="PNG")
        blocos.append((img.width, buf.getvalue()))
    cabecalho = struct.pack("<HHH", 0, 1, len(blocos))
    deslocamento = len(cabecalho) + 16 * len(blocos)
    entradas, dados = b"", b""
    for px, bruto in blocos:
        entradas += struct.pack("<BBBBHHII", px % 256, px % 256, 0, 0, 1, 32,
                                len(bruto), deslocamento + len(dados))
        dados += bruto
    caminho.write_bytes(cabecalho + entradas + dados)


# --- os arquivos que o index.html referencia -------------------------------
icone(32, cor=1.25).save(DESTINO / "favicon-32.png")
icone(180, BG, 0.94).save(DESTINO / "apple-touch-icon.png")
icone(512, BG, 0.80).save(DESTINO / "og-image.png")
salvar_ico(DESTINO / "favicon.ico", [
    icone(16, cor=1.30, nitidez=85),
    icone(32, cor=1.25),
    icone(48, cor=1.15),
])

for nome in ("favicon-32.png", "apple-touch-icon.png", "og-image.png", "favicon.ico"):
    print(nome, (DESTINO / nome).stat().st_size, "bytes")
