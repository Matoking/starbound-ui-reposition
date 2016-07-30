#!/usr/bin/env python
import argparse
import os

from starbound_hud_reposition.patch import create_mod

def main():
    parser = argparse.ArgumentParser(
        description="Create a Starbound HUD element repositioning mod file")

    parser.add_argument(
        'top',
        type=int, default=0,
        help="Padding applied to the top side of the game area")
    parser.add_argument(
        'right',
        type=int, default=0,
        help="Padding applied to the right side of the game area")
    parser.add_argument(
        'bottom',
        type=int, default=0,
        help="Padding applied to the bottom side of the game area")
    parser.add_argument(
        'left',
        type=int, default=0,
        help="Padding applied to the left side of the game area")
    parser.add_argument(
        "--output",
        default=os.path.join(
            os.path.dirname(__file__),
            "hud_reposition.zip"),
        help="Path for the generated ZIP file containing the mod"
    )

    args = parser.parse_args()

    zip_data = create_mod({
        "top": args.top,
        "bottom": args.bottom,
        "left": args.left,
        "right": args.right
    })

    with open(args.output, 'wb') as f:
        f.write(zip_data)
        f.close()

    print("Mod created successfully into the path: %s" % args.output)


if __name__ == "__main__":
    main()
