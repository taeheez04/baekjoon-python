# region 10951 A+B - 4 (브5) / sys모듈의 사용, EOF에 (빈 문자열) 대한 이해
# input(): 개행문자를 제거한 뒤 반환
# sys.stdin.readline(): 개행문자까지 포함한 한 줄 전체 / 횟수가 많을수록 좋음
import sys

nums = []

while True:
    line = sys.stdin.readline()  # 입력이 없으면 line == "" 상태(빈 문자열)
    if (
        not line or line.strip() == ""
    ):  # not line = 입력이 완전히 끝났을 때 EOF / line.strip() 앞 뒤 공백 제거 즉, 엔터만 입력한 경우
        break
    a, b = map(int, line.split())
    nums.append(a + b)

for i in nums:
    print(i)
# endregion
# region 10809 알파벳 찾기 (브2) / find() 찾기, chr 정수(아스키 코드) > 문자로, ord 문자 > 정수(아스키 코드)
S = input()
num = []  # 출력을 위해 리스트 정의

for j in range(26):  # 문자를 하나씩 만들어 문자열에 있는지 찾음
    num.append(S.find(chr(ord("a") + j)))  # find 있으면 위치, 없으면 -1 출력

print(*num)
# endregion
# region 1157 단어공부 (브1) / 새로운 모듈, 딕셔너리, count사용 조건
from collections import Counter  # Counter을 사용하기 위한 모듈

word = input().upper()
result = Counter(word)  # 각 알파벳 갯수를 셈 / 딕셔너리 형태로

max_value = max(result.values())  # 가장 큰 values값 찾기
count = list(result.values()).count(
    max_value
)  # 갯수 구하기 / count는 리스트 전용 메소드

if count == 1:
    for i in result.items():  # .items()로 키와 벨류 둘 다 출력
        if i[1] == max_value:  # [1]은 value
            print(i[0])  # [0]은 key
            break  # 찾았으니 종료로 시간단축
else:
    print("?")
# endregion
# region 2941 크로아티아 알파벳 (실5) / strip(), while문
word = input().strip()  # 문자열 양쪽 끝의 공백 제거
croatian = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

count = 0
i = 0
# i의 위치를 강제로 이동시키기에 한 칸씩 이동하는 for문 보다 while이 효율적
while i < len(word):  # dz=는 3글자라서 먼저 확인
    if word[i : i + 3] == "dz=":
        count += 1
        i += 3  # 인덱스를 증가시켜 뒷자리로
    elif word[i : i + 2] in croatian:  # 그 외 2글자 크로아티아 알파벳
        count += 1
        i += 2
    else:  # 일반 알파벳
        count += 1
        i += 1

print(count)
# endregion
# region 1316 그룹 단어 체커 (실5) / for문과 if문을 적절히 사용, for ~ else문에 대해, 문법을 차근차근
N = int(input())

result = 0

for i in range(N):
    word = input().strip()
    a = []  # 단어마다 새로작성
    prev = word[0]  # 첫 알파벳은 조건충족으로 넘김
    for j in word[1:]:
        if j != prev:  # 단어가 이전단어와 충돌하지 않으면서
            if j not in a:  # a[]안에 들어있지 않을 때
                a.append(prev)  # 이전단어를 a[]에 추가하고
                prev = j  # 이전단어를 바꾼다
            else:
                break
    else:  # break가 1번이라도 실행되지 않았을 때
        result += 1

print(result)
# endregion
# region 25206 너의 평점은 (실5) / 딕셔너리의 제대로 된 사용
# 전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값
subject_avg = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}

subject = 0
subject_score = 0

for i in range(20):
    name, score, grade = (
        input().split()
    )  # map함수는 타입이 int나 float로 일정할 때 사용
    score = float(score)
    if grade == "P":
        continue  # 제외해야하기에 continue
    elif grade in subject_avg:  # 등급이 딕셔너리에 존재할때
        subject_score += score * subject_avg[grade]  # 학점 x 과목평점
        subject += score  # 학점 누적

avg = subject_score / subject  # 전공평점
print(avg)
# endregion
# region 2566 최댓값 (브3) / 리스트로써의 행렬은 넘파이와 다르다
nums = []

for _ in range(9):
    nums.append(list(map(int, input().split())))

max_num = nums[0][0]  # 1번째칸을 초기값으로
line_num = 0  # 행 (가로)
row_num = 0  # 열 (세로)

for i in range(9):
    for j in range(9):
        if nums[i][j] > max_num:  # 리스트 행렬 접근방법
            max_num = nums[i][j]
            line_num = i
            row_num = j

print(max_num)
print(line_num + 1, row_num + 1)  # 1열1행부터 시작하기에
# endregion
# region 10798 세로읽기 (브1) / for _ in range()를 보는 또다른 시각
word = []

for _ in range(5):
    word.append(list(input()))

max_len = len(word[0])

for a in range(1, 5):
    if max_len < len(word[a]):
        max_len = len(word[a])  # word배열들 중에 긴 인덱스를 찾음

for i in range(max_len):  # 이를 반복문에 넣기
    for j in range(5):  # 열은 5줄로 통일
        if i < len(word[j]):  # 해당 줄의 길이가 i보다 길 때만 출력
            print(word[j][i], end="")
# endregion
# region 2563 색종이 (실5) %풀지못함% / 배열로 생각할 것, 리스트 축약
N = int(input())

paper = [[0] * 100 for _ in range(100)]  # 모든 칸이 0인 도화지

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1  # 페이퍼의 값을 1로 변경 이를 통해 겹침을 반복하지 않음

area = 0
for i in range(100):  # 넓이 계산
    for j in range(100):
        if paper[i][j] == 1:
            area += 1

print(area)
# endregion
# region 2745 진법 변환 (브2) / isdigit()의 등장 (문자열에서 숫자 찾기), type의 중요
N, B = input().split()
B = int(B)
N = list(N)  # N은 하나씩 뽑아쓰기 위해 list형태로

result = 0
index = len(N) - 1  # 지수(제곱) / N의 갯수보다 1작아야 계산식이 맞음

for i in N:
    if i.isdigit():  # str형태지만 숫자로만 이뤄진 경우 True / 의미 판단을 위해 사용
        num = int(i)  # str > int형태 바꿈
        result += num * (B**index)  # 그 수의 진법 변환 계산식
    else:
        num = ord(i) - 55  # 문자인 i가 숫자로 변함 / A = 10인 점을 감안해 -55을 해줌
        result += num * (B**index)
    index -= 1

print(result)
# endregion
# region 11005 진법 변환 2 (브1) / 다른 풀이로 문제 이해도 확장
N, B = map(int, input().split())

a = []
while N > 0:
    num = N // B
    a.append(N % B)  # N이 B로 나눠지지 않을 때까지 나머지들 모으기
    N = num
# %처음에는 (N >= B)를 해 while문 밖에 a.append(N)을 적어뒀음%
for i in a[::-1]:  # 마지막 계산된 몫이 맨 앞자리이기에 역순으로
    if i >= 10:
        print(chr(i + 55), end="")
    else:  # i가 정수일 때
        print(i, end="")


# 재귀 풀이: 큰 풀이 안에 작은 풀이 안에 더 작은 풀이... 으로 순서 역순없이 출력을 만듦
def convert(N, B):
    if N < B:  # 종료 조건: 더 이상 쪼갤 수 없을 때
        if N >= 10:
            print(chr(N + 55), end="")
        else:
            print(N, end="")
        return

    convert(N // B, B)  # 이게 해결되야 밑으로 이동

    r = N % B
    if r >= 10:
        print(chr(r + 55), end="")
    else:
        print(r, end="")


N, B = map(int, input().split())
convert(N, B)
# endregion
# region 1193 분수찾기 (실5) / %풀지못함%
X = int(input())

line = 0
total = 0

while total < X:
    line += 1  # 열을 하나씩 늘려
    total += line  # 그 열의 끝 숫자를 구함

pos = X - (total - line)  # X가 그 열에서 몇 번째인지를 구함

if line % 2 == 0:  # 짝수 대각선
    numerator = pos  # 분자
    denominator = line - pos + 1  # 분모
else:  # 홀수 대각선
    numerator = line - pos + 1
    denominator = pos

print(f"{numerator}/{denominator}")
# endregion
# region 2869 달팽이는 올라가고 싶다 (브1) / 반복문(시간초과)이 아니라 계산만을 통해 값을 빠르게 도출
A, B, V = map(int, input().split())

if A >= V:
    print(1)
else:  # 마지막 날을 다르게 생각해야함
    day = (V - A + (A - B) - 1) // (A - B) + 1
    print(day)
# endregion
# region 9506 약수들의 합 (브1) / for문으로 리스트에 넣는다 = 리스트축약, join 문자열을 이어 붙혀
import sys

nums = []

while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break

    a = [i for i in range(1, n) if n % i == 0]  # 리스트 축약

    if sum(a) == n:  # 리스트 a의 합계 = sum(a)
        nums.append(
            f"{n} = " + " + ".join(map(str, a))
        )  # join 구분자를 통해, 여러 문자열을 하나로 이어붙이는 함수 / ex) + 구분자를 이용해 map(str, a)를 이어 붙힘
    else:
        nums.append(f"{n} is NOT perfect.")

for j in nums:
    print(j)
# endregion
# region 11653 소인수분해 (브1) / gpt / 소수를 구할때는 루트로 생각할 것
N = int(input())

# N이 합성수라면 a X b의 곱을 가지는 데 a와 b는 루트N보다 작은 수가 하나는 존재한다
i = 2
while i * i <= N:  # 루트N의 소수를 구한다
    while N % i == 0:
        print(i)
        N //= i
    i += 1

if N > 1:
    print(N)


# endregion
# region 9063 대지 (브3) / set의 활용으로 리스트 안 중복 확인
def all_same(lst):
    return len(set(lst)) == 1  # set은 중복을 제거 / 전부 같으면 1을 표시


N = int(input())

list_x = []
list_y = []
for i in range(N):
    x, y = map(int, input().split())
    list_x.append(x)
    list_y.append(y)

if all_same(list_x) or all_same(list_y):  # 리스트 안의 값이 전부 같은지 다른지 확인
    print(0)
else:
    s_x = max(list_x) - min(list_x)  # 넓이 구하기
    s_y = max(list_y) - min(list_y)
    print(s_x * s_y)
# endregion
# region 24313 알고리즘 수업 - 점근적 표기 1 (실5) / 수학적으로 혼자 접근해볼 것
a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if a1 > c:  # 이 구간 무조건 불가능
    print(0)
else:
    if a1 * n0 + a0 <= c * n0:  # n = n0일 경우를 확인함
        print(1)
    else:
        print(0)
# endregion
# region 2231 분해합(브2) %풀지못함% / 생성자를 찾을 생각이 복잡해 엄두가 안 났음
N = int(input())

for i in range(1, N + 1):
    A = sum(
        map(int, str(i))
    )  # i를 문자열로 (216 > "2", "1", "6") 바꾸고 int로 바꿔 계산 [2, 1, 6]
    if A + i == N:
        print(i)
        break

if i == N:
    print(0)
# endregion
# region 19532 수학은 비대면강의입니다(브2) / 처음배운 크래머 공식
a, b, c, d, e, f = map(int, input().split())

D = a * e - b * d

x = (c * e - b * f) // D
y = (a * f - c * d) // D

print(x, y)
# endregion
# region 2751 수 정렬하기 (브2) / sys모듈에서 출력 최적화
import sys

N = int(sys.stdin.readline())
num = []

for _ in range(N):
    num.append(int(sys.stdin.readline()))

num.sort()

out = sys.stdout.write  # 출력 최적화
for j in num:
    out(str(j) + "\n")
# endregion
# region 1920 수 찾기 (실4) / 시간초과나 런타임에러는 list대신 set으로
import sys

N = int(sys.stdin.readline())
a = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

for i in b:
    if i in a:
        print(1)
    else:
        print(0)
# endregion
# region 10989 수 정렬하기 3 (브1) / 카운팅, 즉시출력으로 메모리 초과 해결
# 리스트에 담아 sort() > 메모리 초과
# 숫자의 개수만 저장하는 > 카운팅 정렬 활용
import sys

input = sys.stdin.readline  # 입력
output = sys.stdout.write  # 출력

N = int(input())
count = [0] * 10001  # 카운팅 배열 생성 / 숫자가 몇 번 나왔는지 저장

for _ in range(N):  # 숫자 개수 세기
    count[int(input())] += 1  # 숫자 위치의 count + 1

for i in range(1, 10001):
    for _ in range(count[i]):  # count[i]만큼 출력
        output(str(i) + "\n")
# endregion
# region 1181 단어정렬(실5) / 정렬 기준값을 만드는 key, lambda 사용
N = int(input())

count = []
for _ in range(N):
    count.append(input().strip())  # input()는 개행문자가 있어 strip()로 제거

count = list(set(count))  # count안에 중복을 제거
count.sort(key=lambda x: (len(x), x))  # key 1순위 길이 2순위 알파벳 순서
# lambda로 임시함수를 만듦 : 임시 def인 격 / x를 넣어 len(x)와 x를 반환, x = count리스트 단어 하나씩
# "but" > (3, "but") 이런식

for i in count:
    print(i)
# endregion
# region 2577 숫자의 개수 (브2) / 모듈의 사용으로 입력받은 숫자에 0~9가 몇개씩 나타나는 지
from collections import Counter

num = 1
for _ in range(3):
    num *= int(input())

cnt = Counter(str(num))  # Counter를 사용하려면 str형태로 입력 받아야 함

for i in range(10):
    print(cnt[str(i)])
# endregion
# region 4344 펑균은 넘겠지 (브1) / 소수점 3째자리까지 출력하기
C = int(input())

result = []
for _ in range(C):
    A = list(map(int, input().split()))
    avg = (sum(A) - A[0]) / A[0]
    a = 0
    for i in A[1:]:  # 값이 맞더라도 과정을 살필 것
        if avg < i:
            a += 1
    result.append((a / A[0]) * 100)

for j in result:
    print("{:.3f}%".format(j))
# endregion
# region 4673 셀프넘버(실5) / list 하나씩 훌어봄, set 적어두고 찾는 느낌
nums = set()
for i in range(1, 10001):  # 1 ~ 10000까지 d(i)를 구함
    num = i + sum(map(int, str(i)))
    nums.add(num)

for j in range(1, 10001):  # d(i)를 구할 때 나온 모든 수를 빼고 출력함
    if j not in nums:
        print(j)
# endregion
# region 2839 설탕배달 (실4) / for-range(start, end, step) 다시 복기
N = int(input())

for five in range(N // 5, -1, -1):
    if (N - five * 5) % 3 == 0:
        print(five + (N - five * 5) // 3)
        break
else:
    print(-1)
# endregion
# region 9095 1, 2, 3 더하기 (실3) / 재귀사고 > 이를 점화식으로 표현
T = int(input())

for _ in range(T):
    n = int(input())
    dp = [0] * (n + 1)

    if n >= 1:
        dp[1] = 1
    if n >= 2:
        dp[2] = 2
    if n >= 3:
        dp[3] = 4

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    print(dp[n])
# endregion
