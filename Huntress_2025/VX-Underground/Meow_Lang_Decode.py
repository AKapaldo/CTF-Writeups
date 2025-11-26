from pathlib import Path

decoded = ''.join(
    chr(s.count('Meow'))
    for s in Path('cute-kitty-noises.txt').read_text().replace(';;',';').split(';')
    if 32 <= s.count('Meow') <= 126
)

print(decoded)
