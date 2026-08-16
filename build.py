import base64, pathlib, sys
D=pathlib.Path("/mnt/skills/examples/canvas-design/canvas-fonts")
FACES=[("Jura","Jura-Light.ttf",300,"normal"),
       ("Jura","Jura-Medium.ttf",500,"normal"),
       ("Outfit","Outfit-Regular.ttf",400,"normal"),
       ("Poiret One","PoiretOne-Regular.ttf",400,"normal"),
       ("Instrument Serif","InstrumentSerif-Regular.ttf",400,"normal"),
       ("Work Sans","WorkSans-Regular.ttf",400,"normal"),
       ("Work Sans","WorkSans-Italic.ttf",400,"italic"),
       ("Work Sans","WorkSans-Bold.ttf",700,"normal"),
       ("DM Mono","DMMono-Regular.ttf",400,"normal")]
css="\n".join(
 f'@font-face{{font-family:"{f}";font-style:{st};font-weight:{w};font-display:swap;'
 f'src:url(data:font/ttf;base64,{base64.b64encode((D/fn).read_bytes()).decode()}) format("truetype")}}'
 for f,fn,w,st in FACES)
src=pathlib.Path("src.html").read_text()
assert "/*FONTS*/" in src, "placeholder ausente"
out=pathlib.Path("salt-cristal.html")
out.write_text(src.replace("/*FONTS*/",css))
print("build ok:", round(out.stat().st_size/1024), "KB |", len(FACES), "faces")
