# 감소하는 수 인지 체크
def gumsa(num):
    while num > 9:
        t = num % 10
        num //= 10
        if num % 10 <= t:
            return False
    return True
        

N = int(input())  # 몇번째 감소하는 수?

if N > 1022:  # 1022 => 9876543210 이므로 그 이상은 없다!!
    print(-1)
elif N < 11:  # 0 ~ 10 은 모두 감소하는 수이므로 그대로 출력!!
    print(N)
else:  # 일의자리부터 N의자리까지 증가하는 수 인지 체크!!
    x = 10  # 10 다음에 오는 감소하는 수부터 찾기 시작
    while N-10 > 0:  # 0~10은 이미 구했으니 빼주기  (11 <= N <= 1022)
        tmp = x  # 계산용 복사
        k = 0  # 다음 감소하는 수를 구하기 위한 계산 기준  (10의 k승으로 사용)
        while True:
            teil = tmp % 10  # 맨 뒤자리 수
            tmp //= 10  # 맨 뒤에서 앞자리 구하기 위해 10으로 나눠주기
            if tmp % 10 > teil + 1:  # 맨 뒤에서 앞자리가 맨뒤자리에 1더한 값보다 크면 그 값이 *다음 감소하는 수*  => 20 다음은 21
                break
            else:  # 아니면 다시 그 앞자리와 비교해야 한다!!
                x = tmp * (10 ** (k+1))  # 그렇다면 뒤자리수는 0으로 초기화작업 필요!  => 이 작업을 해야 21 다음에 31이 아닌 30이 온다!!
            k += 1  # 비교값이 앞자리로 변경됐으니 k값 증가
            if len(str(x)) - 1 == k:  # x의 자릿수-1이 k와 같아지면 더이상 자릿수 비교 불가 => 맨 앞자리수가 1증가
                break
        x += 10 ** k  # x는 10의 k승만큼 증가 !!  ex) 10의 0승: 20 -> 21 , 10의 1승: 21 -> 30, 10의 2승: 210 -> 310
        if gumsa(x) == False: continue  # 28번줄의 0 초기화작업에 따라 100과 같이 0이 중복되는 수는 건너 뛴다
        N -= 1  # 감소하는 수를 구했다 !! -> N번째를 찾아야 하기에 1감소
        
    print(x)
