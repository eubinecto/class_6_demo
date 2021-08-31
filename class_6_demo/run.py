
import argparse
from transformers import pipeline


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str)
    args = parser.parse_args()
    input_str = args.input
    classifier = pipeline("sentiment-analysis")
    result = classifier(input_str)[0]
    print(result)


if __name__ == '__main__':
    main()
