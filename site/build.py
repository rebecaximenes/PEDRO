#!/usr/bin/env python3
"""Gera o site das casas a partir de src.html.

  python3 build.py                       -> index.html (página completa, autocontida)
  python3 build.py --artifact saida.html -> também grava a versão sem <html>/<head>,
                                            no formato aceito pelo publicador de Artifacts

As fontes entram embutidas em base64: o arquivo final não depende de rede.
"""
import argparse, base64, pathlib, re, sys

AQUI = pathlib.Path(__file__).resolve().parent
FONTES_DIR = pathlib.Path("/mnt/skills/examples/canvas-design/canvas-fonts")

FACES = [
    ("Italiana",   "Italiana-Regular.ttf",  400, "normal"),
    ("Work Sans",  "WorkSans-Regular.ttf",  400, "normal"),
    ("Work Sans",  "WorkSans-Bold.ttf",     700, "normal"),
    ("DM Mono",    "DMMono-Regular.ttf",    400, "normal"),
]

META = {
    "titulo": "Ocre & Gris — Casas em São Miguel dos Milagres",
    "descricao": ("Duas casas inteiras de aluguel por temporada em São Miguel dos Milagres, "
                  "na Rota Ecológica de Alagoas. Piscina privativa, camareira diária e "
                  "praia a poucos minutos a pé."),
    "url": "https://ocreegris.com.br/",
}


def css_das_fontes() -> str:
    if not FONTES_DIR.is_dir():
        sys.exit(f"pasta de fontes não encontrada: {FONTES_DIR}")
    regras = []
    for familia, arquivo, peso, estilo in FACES:
        caminho = FONTES_DIR / arquivo
        if not caminho.exists():
            sys.exit(f"fonte ausente: {caminho}")
        b64 = base64.b64encode(caminho.read_bytes()).decode()
        regras.append(
            f'@font-face{{font-family:"{familia}";font-style:{estilo};font-weight:{peso};'
            f'font-display:swap;src:url(data:font/ttf;base64,{b64}) format("truetype")}}'
        )
    return "\n".join(regras)


def montar_pagina(corpo_artifact: str) -> str:
    """Envolve a versão artifact num documento HTML completo."""
    partes = corpo_artifact.split("</style>", 1)
    if len(partes) != 2:
        sys.exit("não achei o fim do bloco <style> em src.html")
    cabeca, corpo = partes[0] + "</style>", partes[1]
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{META['descricao']}">
<meta name="theme-color" content="#F5F1E9">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Ocre &amp; Gris">
<meta property="og:title" content="{META['titulo']}">
<meta property="og:description" content="{META['descricao']}">
<meta property="og:url" content="{META['url']}">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="{META['url']}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%23F5F1E9'/%3E%3Ccircle cx='16' cy='11' r='5' fill='%23B9832F'/%3E%3Cpath d='M4 20h24M4 25h24' stroke='%231D5B55' stroke-width='2' stroke-dasharray='4 3'/%3E%3C/svg%3E">
{cabeca}
</head>
<body>
{corpo}
</body>
</html>
"""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--artifact", metavar="ARQUIVO",
                    help="grava também a versão sem <html>/<head> nesse caminho")
    args = ap.parse_args()

    fonte = (AQUI / "src.html").read_text(encoding="utf-8")
    if "/*FONTS*/" not in fonte:
        sys.exit("placeholder /*FONTS*/ ausente em src.html")

    completo = fonte.replace("/*FONTS*/", css_das_fontes())

    saida = AQUI / "index.html"
    saida.write_text(montar_pagina(completo), encoding="utf-8")
    print(f"index.html    {round(saida.stat().st_size/1024):>5} KB  ({len(FACES)} fontes embutidas)")

    if args.artifact:
        alvo = pathlib.Path(args.artifact)
        alvo.parent.mkdir(parents=True, exist_ok=True)
        alvo.write_text(completo, encoding="utf-8")
        print(f"{alvo.name:<13} {round(alvo.stat().st_size/1024):>5} KB  (formato artifact)")

    # aviso sobre o que ainda falta preencher
    pendentes = len(re.findall(r"<!--\s*CONFIRMAR", fonte))
    if pendentes:
        print(f"\n{pendentes} bloco(s) marcado(s) com <!-- CONFIRMAR --> em src.html")


if __name__ == "__main__":
    main()
