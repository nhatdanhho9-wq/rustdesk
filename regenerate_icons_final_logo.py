#!/usr/bin/env python3
"""
Regenerate ALL 20 Android icon variants from AFKZONE_finalLogo.png
For AFK Zone v2.0.3
"""

from PIL import Image
import os

# Source logo
SOURCE_LOGO = r"D:\n8n-claude\AFKZONE_finalLogo.png"
FLUTTER_DIR = r"D:\n8n-claude\rustdesk-custom\flutter"

# Icon variants and their sizes for each density
ICON_CONFIGS = {
    'mdpi': {
        'ic_launcher.png': 48,
        'ic_launcher_round.png': 48,
        'ic_launcher_foreground.png': 108,
        'ic_stat_logo.png': 24,
    },
    'hdpi': {
        'ic_launcher.png': 72,
        'ic_launcher_round.png': 72,
        'ic_launcher_foreground.png': 162,
        'ic_stat_logo.png': 36,
    },
    'xhdpi': {
        'ic_launcher.png': 96,
        'ic_launcher_round.png': 96,
        'ic_launcher_foreground.png': 216,
        'ic_stat_logo.png': 48,
    },
    'xxhdpi': {
        'ic_launcher.png': 144,
        'ic_launcher_round.png': 144,
        'ic_launcher_foreground.png': 324,
        'ic_stat_logo.png': 72,
    },
    'xxxhdpi': {
        'ic_launcher.png': 192,
        'ic_launcher_round.png': 192,
        'ic_launcher_foreground.png': 432,
        'ic_stat_logo.png': 96,
    }
}

def main():
    print(f"Loading source logo: {SOURCE_LOGO}")
    source = Image.open(SOURCE_LOGO)
    print(f"Source size: {source.size}")

    total_icons = 0
    for density, icons in ICON_CONFIGS.items():
        mipmap_dir = os.path.join(FLUTTER_DIR, 'android', 'app', 'src', 'main', 'res', f'mipmap-{density}')
        print(f"\n{density.upper()} ({len(icons)} icons):")

        for icon_name, size in icons.items():
            # Resize with high quality
            resized = source.resize((size, size), Image.Resampling.LANCZOS)

            # Output path
            output_path = os.path.join(mipmap_dir, icon_name)

            # Save as PNG
            resized.save(output_path, 'PNG', optimize=True)

            file_size = os.path.getsize(output_path)
            print(f"  [OK] {icon_name:30} {size}x{size}  ({file_size:,} bytes)")
            total_icons += 1

    print(f"\n{'='*60}")
    print(f"SUCCESS: Regenerated {total_icons} icons from AFKZONE_finalLogo.png")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
