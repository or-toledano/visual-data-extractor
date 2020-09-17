import sys
from visualextract.extract import extract_data


def main():
    if len(sys.argv) == 1:
        print(extract_data(sys.argv[1]))
    else:
        print("Usage: python -m visualextract <path to image>")


if __name__ == "__main__":
    main()
