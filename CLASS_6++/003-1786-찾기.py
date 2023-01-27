import sys


def brute_force(src: str, search: str) -> list:
    ret = []
    begin = 0
    while (begin + len(search) <= len(src)):
        matched = True
        for i in range(len(search)):
            if src[begin + i] != search[i]:
                matched = False
                break

        if matched:
            ret.append(begin+1)
            
        begin += 1
    
    return ret


def get_partial_match(search: str) -> list:
    M = len(search)
    pi = [0] * M

    begin = 1; matched = 0

    while begin + matched < M:
        # 탐색 문자열이 탐색 문자열 자신과 비교
        if search[begin + matched] == search[matched]:
            matched += 1
            pi[begin + matched - 1] = matched
            # 같으면 접두 접미 배열 갱신
        
        else:
            if matched == 0:
                begin += 1
            else:
                ## KMP 문자열 탐색 알고리즘 과 동일하게 불일치 발생 시
                ## 매칭을 진행하면서 구했던 접두 접미사 길이 만큼 탐색을 건너뛸 수 있다
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]

    return pi


def KMP_search(src: str, search: str) -> list:
    ret = []

    N = len(src); M = len(search)

    # 탐색할 문자열의 접두사, 접미사 길이를 문자열의 처음부터 끝 까지 미리 계산
    pi = get_partial_match(search)

    begin = 0; matched = 0;
    while begin <= N - M:
        # 탐색할 문자열과 원본 문자열에서 현재 위치의 문자가 동일한 경우
        if matched < M and src[begin + matched] == search[matched]:
            matched += 1

            # 문자열이 모두 일치
            if matched == M:
                ret.append(begin + 1)

        else:
            # 일치하는 부분이 없는 경우, 다음 위치의 문자부터 탐색
            if matched == 0:
                begin += 1

            # 접두사 점미사 같은 만큼 건너 뛰게 함
            else:
                # 현재 불일치가 일어난 위치 begin + matched
                # 여기서 접두, 접미사의 길이인 pi[matched - 1] 을 빼주면 다음 탐색 시작 위치
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    
    return ret


def main():
    input = sys.stdin.readline
    result_list = KMP_search(input().rstrip(), input().rstrip())
    print(len(result_list))
    print(*result_list)


if __name__ == '__main__':
    main()