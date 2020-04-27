from pathlib import Path

p = Path('.')
mds = list(p.glob('output_*.md'))

for md in mds:

    path = "./" + md.name
    Path(path).unlink()
