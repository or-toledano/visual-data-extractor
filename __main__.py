import sys
from visualextract.extract import extract_data


def main():
    if len(sys.argv):
        print(extract_data(sys.argv[1]))


if __name__ == "__main__":
    main()

