def what(N):

    global max_N
    global i
    n = i
    i += 1
    # i 번째 호출 일때 출력은 가장 작은 단위 일 때부터 출려됨
    if i == max_N: #
        # 최대로 ____ 출력
        print(f"{'____'*(i)}\"재귀함수가 뭔가요?\"")
        print(f"{'____' * (i)}\"재귀함수는 자기 자신을 호출하는 함수라네\"")
        print(f"{'____' * (i)}라고 답변하였지.")
        return


    print(f"{'____' * i}\"재귀함수가 뭔가요?\"")
    print(f"{'____' * i}\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
    print(f"{'____' * i}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
    print(f"{'____' * i}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
    what(N)
    print(f"{'____' * (n+1)}라고 답변하였지.") # 이 문구는 N, N-1,..2,1 0 이렇게 출력

    return

N = int(input())
i = -1
max_N = N
print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
what(N)