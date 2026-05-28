import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from PIL import Image, ImageDraw
import os

SRC = r'd:\GITHUB\FOCO_DE_BATALHA\www\img\capa.png'
RES = r'd:\GITHUB\FOCO_DE_BATALHA\android\app\src\main\res'
BG  = (1, 8, 17)  # #010811

DENSITIES = [
    ('mipmap-mdpi',    48,  108),
    ('mipmap-hdpi',    72,  162),
    ('mipmap-xhdpi',   96,  216),
    ('mipmap-xxhdpi',  144, 324),
    ('mipmap-xxxhdpi', 192, 432),
]

src = Image.open(SRC).convert('RGBA')
w, h = src.size
crop_size = min(w, h)
left = (w - crop_size) // 2
sq = src.crop((left, 0, left + crop_size, crop_size))

for folder, plain_px, fg_px in DENSITIES:
    path = os.path.join(RES, folder)
    os.makedirs(path, exist_ok=True)

    # ic_launcher_foreground.png — canvas 108dp, arte na safe zone (72dp = 66.7%)
    canvas = Image.new('RGBA', (fg_px, fg_px), (0, 0, 0, 0))
    safe = int(fg_px * 72 / 108)
    pad  = (fg_px - safe) // 2
    art  = sq.resize((safe, safe), Image.LANCZOS)
    canvas.paste(art, (pad, pad), art)
    canvas.save(os.path.join(path, 'ic_launcher_foreground.png'))

    # ic_launcher.png — fundo escuro + arte
    plain = Image.new('RGBA', (plain_px, plain_px), BG + (255,))
    art2  = sq.resize((plain_px, plain_px), Image.LANCZOS)
    plain.paste(art2, (0, 0), art2)
    plain.save(os.path.join(path, 'ic_launcher.png'))

    # ic_launcher_round.png — circular com fundo escuro
    mask = Image.new('L', (plain_px, plain_px), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, plain_px - 1, plain_px - 1), fill=255)
    bg_rnd = Image.new('RGBA', (plain_px, plain_px), BG + (255,))
    bg_rnd.paste(plain, (0, 0))
    bg_rnd.putalpha(mask)
    final = Image.new('RGBA', (plain_px, plain_px), BG + (255,))
    final.paste(bg_rnd, (0, 0), bg_rnd)
    final.save(os.path.join(path, 'ic_launcher_round.png'))

    print(f'OK {folder}: launcher={plain_px}px  foreground={fg_px}px')

print('Adaptive icons gerados.')
