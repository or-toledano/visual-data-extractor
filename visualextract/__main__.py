import sys
import argparse

from visualextract.extract import extract_data


def main():
    parser = argparse.ArgumentParser(description='Extract data from quads')
    parser.add_argument('--path', help='path to the image with quads',
                        required=True)
    parser.add_argument('--rotate', help='try all rotations of the quads',
                        action='store_true', default=False)
    args = parser.parse_args()

    for text in extract_data(args.path, rotate=args.rotate):
        print(text)


if __name__ == "__main__":
    main()
