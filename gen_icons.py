from PIL import Image
import os

src = "www/icons/icon-512.png"
base = "android/app/src/main/res"

sizes = {
    "mipmap-mdpi":    (48, 108),
    "mipmap-hdpi":    (72, 162),
    "mipmap-xhdpi":   (96, 216),
    "mipmap-xxhdpi":  (144, 324),
    "mipmap-xxxhdpi": (192, 432),
}

img = Image.open(src).convert("RGBA")
for folder, (launcher_sz, fg_sz) in sizes.items():
    out = os.path.join(base, folder)
    os.makedirs(out, exist_ok=True)
    img.resize((launcher_sz, launcher_sz), Image.LANCZOS).save(os.path.join(out, "ic_launcher.png"))
    img.resize((launcher_sz, launcher_sz), Image.LANCZOS).save(os.path.join(out, "ic_launcher_round.png"))
    img.resize((fg_sz, fg_sz), Image.LANCZOS).save(os.path.join(out, "ic_launcher_foreground.png"))
    print(f"  {folder}: ok")

print("DONE")
