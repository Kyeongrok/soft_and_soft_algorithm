#1의자리 2의자리 3의자리 4의자리

def solution(pw):
    cnt = 0
    for l in range(10):
        for k in range(10):
            for j in range(10):
                for i in range(10):
                    cnt += 1
                    print(f'{l}{k}{j}{i}')
    print(cnt)

solution(3247)