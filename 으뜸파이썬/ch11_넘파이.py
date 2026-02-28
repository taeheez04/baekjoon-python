# 11.1 넘파이 라이브러리: 외부 패키지, 머신러닝 분야, 행렬 계산
import numpy as np # 프롬프트에 pip install numpy 입력 후 할 것 (작동이 안될 경우)
a = np.array([1, 2, 3], dtype=np.int32) # 32비트로 속성값 지정
b = np.array([4, 5, 6], dtype="int64") # defualt값 64비트 / 속성값 지정의 2가지 방법
print(type(a))
print(a) # 출력 환경 차이로 [1, 2, 3]으로 출력됨
print(a.shape) # 객체의 형태
print(a.ndim) # 객체의 차원
print(a.dtype) # 객체 내부 자료형
print(a.itemsize) # 객체 내부 자료형이 차지하는 메모리 크기(byte)
print(a. size) # 객체의 전체 크기(항목의 수)
c = a + b
print(b.dtype)
print(c.dtype)
print()
#-------------------------------------------------------------------
# 11.2 ndarray의 메소드와 주요 함수
# 배열의 연산에 관련된 40여개의 메소드들이 지원됨 ex) max(), min(), mean()
a = np.array([[1, 1], [2, 2], [3, 3]])
print(a.flatten()) # 배열의 평탄화 = 1차원으로 만듦

a = np.array([1, 2, 3])
b = np.array([[4, 5, 6], [7, 8, 9]])
print(np.append(a, b)) # axis 축을 명시하지 않아 평탄화 작업을 수행함
print(np.append([a], b, axis = 0)) # 축의 명시로 차원이 생김 but 차원이 다를 경우 오류 발생 (추후 설명)
# 랜덤함수로 난수 생성도 가능(ex: np.random.rand(0, 10, size = 10))
print()
#-------------------------------------------------------------------
# 11.3 ndarray의 연산 / 사칙연산 다 가능 // 단순 곱과 행렬 곱은 다름
a = np.array([[1, 2], [3, 4]])
b = np.array([[10, 20], [30, 40]])
c = a * b
print(c) # 차원, 자료형 같아 단순 곱
print(np.matmul(a, b))
print(a @ b) # 행렬 곱 함수들(가로 x 세로 이런 식)
print(a + 1) # 행렬 각 성분에 대한 덧셈
print()
#-------------------------------------------------------------------
# 11.4 ndarray의 생성: n x m 행렬 생성 (이중괄호 주의)
print(np.zeros((2, 3))) # 초기값 0
print(np.ones((2, 3))) # 초기값 1
print(np.full((2, 3), 100)) # 초기값 지정
print(np.eye(3)) # 대각성 성분 1, 나머지 0인 단위행렬
print(np.random.random((2, 3))) # 0 ~ 1사이 실수를 초기값으로

print(np.arange(0, 10, 2)) # 0 ~ 9 사이 2칸씩
print(np.linspace(0, 10, 5)) # 0 ~ 10 사이 동일한 간격으로 5회 생성
print()
#-------------------------------------------------------------------
# 11.5 ndarray의 재구성
print(np.arange(0, 10).reshape(2, 5)) # reshape안의 열과 행이 갯수와 맞아야 함
print(np.arange(0, 24).reshape(4, 3, 2)) # 4차원 3열 2행

print(np.arange(6).reshape(3, 2).transpose()) # 행과 열이 변경됨
print()
#-------------------------------------------------------------------
# 11.6 다차원 배열의 축: axis(방향) / n차원 배열의 경우 n개의 축을 가진 (차원 : axis 0 세로, axis 1 가로, axis 2는 z축 ~)
print(np.arange(0, 6).reshape(3, 2))
print(np.arange(0, 6).reshape(3, 2).sum(axis = 0)) # 세로 합
print(np.arange(0, 6).reshape(3, 2).sum(axis = 1)) # 가로 합 / min, max등도 가능

a = np.array([1, 3, 4])
print(np.insert(a, 1, 2)) # a 인덱스 1번째에 2 삽입
b = np.array([[1, 1], [2, 2], [3, 3]])
print(np.insert(b, 1, 4, axis = 0)) # b 인덱스 1번째에 4를 axis = 0으로 삽입 / 4 대신 (4, 4)를해도 동일
print(np.insert(b, 1, 4, axis = 1)) # b 인덱스 1번째에 4를 axis = 1으로 삽입 
print()
#-------------------------------------------------------------------
# 11.7 배열의 인덱싱과 슬라이싱 / 1차원은 리스트 인덱싱, 슬라이싱과 같다
a = np.array([1, 2, 3, 4, 5])
print(a[np.array([0, 1])])
print(a[np.array([1, 1, 1, 1])])

print(a[1:5])
print(a[::-1])
print()
#-------------------------------------------------------------------
# 11.8 2차원 배열의 인덱싱
a = np.arange(0, 6).reshape(3, 2) # 2차원
print(a)
print(a[0, 0])
print(a[0]) # 행을 찾음

b = np.arange(0, 24).reshape(4, 3, 2) # 3차원
print(b)
print(b[1, 2, 1])
print(b[0]) # 차원을 찾음
print(b[0, 0]) # 차원에서 행을 찾음

print(np.concatenate((b[0, 0], b[0, 2]), axis = 0)) # 차원이 1개라 axis = 0
print(np.concatenate((b[0, 0].reshape(1, 2), b[0, 2].reshape(1, 2)), axis=1)) # 2차원으로 만들어 axis = 1이 가능
print()
#-------------------------------------------------------------------
# 11.9 2차원 배열의 슬라이싱
a = np.arange(0, 9).reshape(3, 3)
print(a)
print(a[0, :]) # 행, 열
print(a[:, 0])
print(a[0, 0:2])
print(a[0, 1:2])
print(a[1, 1:].shape) # 1차원
print(a[1:2, 1:].shape) # 2차원
print()
#-------------------------------------------------------------------
# 11.10 선형 방정식 풀이, 행렬식
import numpy as np

a = np.array([[2, 3], [1, -2]]) # 연립 방정식을 품
b = np.array([1, 4])
x = np.linalg.solve(a, b) # x와 y의 값을 구함
print(x)

a = np.array([[1, 2], [3, 4]])
print(np.linalg.det(a)) # 행렬식 구함