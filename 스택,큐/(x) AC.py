# https://www.acmicpc.net/problem/5430
from collections import deque
t = int(input()) # 테스트 케이스의 수
for _ in range(t):
    move = input() # 문제에서 주어진 수행할 함수
    n = int(input()) # 배열에 들어있는 수의 개수
    arr = input()[1:-1].split(',')
     # [1,2,3,4]를 입력하면 [과 ]는 0,-1 index이므로 인식하지 않는다.
    q = deque(arr)
    # 뒤집는 수를 담을 변수, 한 동작을 돌때 뒤집는 것보다 총 수를 합하여 한꺼번에 뒤집는 것이 메모리를 아낄 수 있다.
    cnt = 0 
    if n == 0:
        q = []
    for m in move:
        if m == 'R':
            cnt += 1
        elif m == 'D':
            if len(q) == 0: #  배열이 비어있는데 D를 사용한 경우, 에러가 발생
                print('error')
                break
            else:
                if cnt % 2 == 0:
                    q.popleft()
                else:
                    q.pop() 
    # for-else문 : for문이 break등으로 중간에 빠져나오지 않고 끝까지 실행되었을때 수행                     
    else:                
        if cnt % 2 == 0:
            print('[' + ','.join(q) + ']')
        else:
            q.reverse() # 총 뒤집는 수가 홀수인 경우 move를 반복문 돌린 결과에서 뒤집어줘야한다.
            print('[' + ','.join(q) + ']')  
        # ex) [1,2,3,4] RDD -> R 1번 (홀수) 
        # 반복문 수행 -> D D -> [1,2] -> R은 홀수이므로 마지막에 뒤집어서 결과를 출력한다.              





