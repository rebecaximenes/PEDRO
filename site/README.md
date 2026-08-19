# Ocre & Gris — site de aluguel por temporada

Site de página única para as duas casas de São Miguel dos Milagres, Alagoas:
[@casaocremilagres](https://www.instagram.com/casaocremilagres/) e
[@casagrismilagres](https://www.instagram.com/casagrismilagres/).

## Arquivos

| Arquivo | O que é |
| --- | --- |
| `src.html` | fonte editável. É aqui que se mexe. Tem o placeholder `/*FONTS*/`. |
| `build.py` | injeta as fontes em base64 e gera o `index.html`. |
| `index.html` | **gerado** — página completa e autocontida, pronta para subir. Não editar à mão. |

```bash
python3 build.py                          # gera index.html
python3 build.py --artifact preview.html  # gera também a versão sem <html>/<head>
```

O `index.html` final não faz nenhuma requisição de rede: fontes, ícones e ilustrações
estão todos embutidos. Basta jogar o arquivo em qualquer hospedagem estática
(Netlify, Vercel, GitHub Pages, Hostinger) ou abrir direto no navegador.

## Antes de publicar

O conteúdo estrutural está pronto; o que falta são os dados reais das casas.
No `src.html`, cada trecho a revisar está marcado com `<!-- CONFIRMAR -->`.

- [ ] **WhatsApp e e-mail** — no bloco `CONFIG`, no fim do `src.html`.
      O número vai só com dígitos: `55` + DDD + número.
- [ ] **Ficha da Casa Ocre** — suítes, hóspedes, banheiros, m², piscina, distância do mar.
- [ ] **Ficha da Casa Gris** — idem.
- [ ] **Lista de ambientes e comodidades** de cada casa.
- [ ] **Tabela de diárias** — valores, períodos de temporada e mínimo de noites.
- [ ] **Textos de cada casa** — os parágrafos atuais são uma primeira versão, escritos a
      partir do que os nomes sugerem, e devem ser conferidos.
- [ ] **Distâncias e tempos** citados em "A região" e "Como chegar".
- [ ] **Domínio** — trocar `https://ocreegris.com.br/` no dicionário `META` do `build.py`.

## Trocar os blocos de foto por fotos de verdade

Todo espaço reservado para imagem é uma `div.foto` com um desenho de marca-d'água:

```html
<div class="foto" data-tom="ocre" data-legenda="foto · piscina e varanda">
  <svg class="marca-dagua" viewBox="0 0 120 90" style="color:#8A5F1C"><use href="#m-piscina"/></svg>
</div>
```

Para colocar a foto, basta acrescentar um `<img>` dentro da `div` — o CSS já cobre o bloco
inteiro e esconde a legenda:

```html
<div class="foto" data-tom="ocre" data-legenda="foto · piscina e varanda">
  <img src="fotos/ocre-piscina.jpg" alt="Piscina e varanda da Casa Ocre" loading="lazy">
</div>
```

Se as fotos ficarem numa pasta `fotos/` ao lado do `index.html`, o site deixa de ser um
arquivo só — é o único momento em que isso acontece. Recomendado: JPEG a 1600 px de
largura, com qualidade 80.

## Como o site está montado

| Seção | Âncora | Conteúdo |
| --- | --- | --- |
| Capa | `#capa` | wordmark, frase de posicionamento e quatro números-chave |
| Manifesto | `#sobre` | onde fica, e o que diferencia casa inteira de pousada |
| As casas | `#casas` | os dois cartões, um para cada casa |
| Casa Ocre | `#ocre` | galeria, ficha técnica, ambientes, comodidades |
| Casa Gris | `#gris` | mesma estrutura, na paleta cinza |
| Diárias | `#diarias` | tabela por temporada, o que inclui, regras de reserva |
| A região | `#regiao` | seis experiências da Rota Ecológica |
| Como chegar | `#chegar` | as quatro etapas entre o aeroporto e a chave na mão |
| Dúvidas | `#duvidas` | sete perguntas frequentes |
| Reserva | `#reserva` | formulário que abre o WhatsApp já preenchido |

O formulário não tem servidor: ele monta a mensagem e abre `wa.me`. Nada é armazenado,
nada é enviado para terceiros.

## Identidade

A paleta sai dos nomes das casas: **ocre** (`#B9832F`) para a primeira, **gris**
(`#66757A`) para a segunda, sobre uma base de areia (`#F5F1E9`) e com verde-mar
(`#1D5B55`) nas ações. Cada casa é reconhecível pela cor antes de se ler o nome.

Tipografia: **Italiana** nos títulos, **Work Sans** no texto corrido e **DM Mono** nos
rótulos e números. A linha tracejada que atravessa o site é a linha de recifes — a mesma
que transforma o mar em piscina na maré baixa.
