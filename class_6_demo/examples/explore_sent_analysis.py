
from transformers import pipeline


def main():
    # 아마도 사전훈련된 모델을 다운로드할 것.
    classifier = pipeline("sentiment-analysis")
    result = classifier("I love this product")[0]
    print(result)


if __name__ == '__main__':
    main()

