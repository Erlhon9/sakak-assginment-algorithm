# SAKAK Backend Position Assignment - Algorithm

## 실행 방법 (Python 3.12)

1. library 설치

```bash
pip install -r requirements.txt
```

2. 실행

```bash
pytest
```

## 풀이에 대한 설명

- solution1: `look_and_say_sequence_recursive`
    
    가장 직관적인 방법을 이용해서 풀이했습니다.

    n을 점차 키워나가면서 이전의 값들을 통해 새로운 값을 구하는 방식으로 풀이했습니다.

- solution2: `look_and_say_sequence_iterative`

    재귀함수를 이용하지 않고 반복문을 이용해서 풀이했습니다.
