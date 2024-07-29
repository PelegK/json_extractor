from json_extractor import *


def main():
    path = Path('data/python_exercise.json')
    extractor = JsonExtractor(path)
    extracted = extractor.dataExtractor()


if __name__ == "__main__":
    main()
