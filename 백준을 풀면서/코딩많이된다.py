# region 10250 ACM호텔 (브3)
T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    room = []
    for i in range(1, W + 1):
        for j in range(1, H + 1):
            room.append((j * 100) + (i))
    print(room[N - 1])
# endregion
# 이 문제를 방을 만들어 손님을 넣는거 말고
# 손님을 바로 방으로 안내하는 방향으로 작성해볼 것
