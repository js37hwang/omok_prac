from constants import Stone, JudgeNum, JudgeDirection

# 사용자가 돌을 넣으려는 좌표를 가지고 검사를 진행할 바둑판 범위 구하기
# 돌을 두려는 좌표를 중심으로
# 오목의 경우 9x9 (5*2-1)
# 육목의 경우 11x11 (6*2-1)
# 33의 경우 5x5(3*2-1) 안에서 연속된 3개가 다른 방향으로 2개가 나와야 함
# 이때 오목판 19*19 범위 밖은 검사할 필요가 없음
# 좌표를 중심으로 위/아래/가로/세로 범위- 오목의 경우 5-1로 진행


def GetCheckRange(row, col, panRowCnt, max_stones):
    """
    row: 가로 좌표
    col: 세로 좌표
    panRowCnt: 오목판(정사각형)의 가로
    max_stones: 수만큼 연속으로 존재 시 true 리턴
    """

    steps = max_stones - 1  # 이미 돌이 하나 놓인 상태이므로 -1
    lastIndex = panRowCnt - 1  # 오목판의 마지막 idx

    # 입력받은 좌표를 중심으로 바둑판 내에서 검사 범위 설정 진행
    minRowRange = 0 if row - steps < 0 else row - steps
    maxRowRange = lastIndex if row + steps > lastIndex else row + steps

    minColRange = 0 if col - steps < 0 else col - steps
    maxColRange = lastIndex if col + steps > lastIndex else col + steps

    return {minRowRange, maxRowRange, minColRange, maxColRange}


# 구한 검사 범위를 가지고 게임 승리 해당 여부확인 진행
def CheckWin(
    minRowRange,
    maxRowRange,
    minColRange,
    maxColRange,
    max_stones,
    currentPlayer,
    omok_pan,
):
    """
    minRowRange: 행 최소 좌표
    maxRowRange: 행 최대 좌표
    minColRange: 열 최소 좌표
    maxColRange: 열 최대 좌표

    max_stones
    currentPlayer
    """

    # 가로 검사
    for i in range(minRowRange, maxRowRange + 1):
        temp = 0
        for j in range(minColRange, maxColRange + 1):

            if omok_pan[i][j] == currentPlayer:
                temp += omok_pan[i][j]
            else:
                temp = 0  # 다른 색 돌 하나라도 있으면 reset

            if abs(temp) == max_stones:
                return True

    # 세로 검사
    for i in range(minColRange, maxColRange + 1):
        temp = 0
        for j in range(minRowRange, maxRowRange + 1):

            if omok_pan[i][j] == currentPlayer:
                temp += omok_pan[i][j]
            else:
                temp = 0  # 다른 색 돌 하나라도 있으면 reset

            if abs(temp) == max_stones:
                return True

    # 슬 검사
    for i in range(maxColRange, minColRange - 1, -1):
        temp = 0
        idx = 0

        if omok_pan[maxRowRange - idx][i] == currentPlayer:
            temp += omok_pan[maxRowRange - idx][i]
        else:
            temp = 0  # 다른 색 돌 하나라도 있으면 reset

        idx += 1

        if abs(temp) == max_stones:
            return True

    # 역슬 검사
    for i in range(minRowRange, maxRowRange + 1):
        temp = 0

        if omok_pan[i][minColRange + 1] == currentPlayer:
            temp += omok_pan[i][minColRange + 1]
        else:
            temp = 0  # 다른 색 돌 하나라도 있으면 reset

        if abs(temp) == max_stones:
            return True
