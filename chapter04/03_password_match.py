#1의자리 2의자리 3의자리 4의자리

def solution(pw):
    pw = str(pw)
    for l in range(10):
        for k in range(10):
            for j in range(10):
                for i in range(10):
                    r = f'{l}{k}{j}{i}'
                    if r == pw:
                        print('찾았습니다.', pw, r)
solution(3247)