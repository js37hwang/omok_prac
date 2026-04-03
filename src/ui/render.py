import pygame
from constants import (
    BOARD_SIZE,
    MARGIN,
    CELL_SIZE,
    BOARD_WIDTH,
    # WINDOW_SIZE,
    WOOD_COLOR,
    WHITE_COLOR,
    BLACK_COLOR,
    Stone,
)


def DrawBoard(screen):
    """바둑판 선 그리기"""

    # 화면 초기화 함수로 fill 함수 미사용 시 이전 화면 잔상이 남음
    screen.fill(WOOD_COLOR)  # 나무색 배경

    for i in range(BOARD_SIZE):
        # 가로줄
        pygame.draw.line(
            screen,
            BLACK_COLOR,
            (MARGIN, MARGIN + i * CELL_SIZE),
            (MARGIN + BOARD_WIDTH, MARGIN + i * CELL_SIZE),
        )
        # 세로줄
        pygame.draw.line(
            screen,
            BLACK_COLOR,
            (MARGIN + i * CELL_SIZE, MARGIN),
            (MARGIN + i * CELL_SIZE, MARGIN + BOARD_WIDTH),
        )


def GetBoardPos(mouse_pos):
    """마우스 클릭 좌표(pixel)를 바둑판 인덱스(row, col)로 변환"""
    x, y = mouse_pos
    # 계산식: (좌표 - 여백 + 절반칸) // 칸크기 -> 반올림 효과
    col = (x - MARGIN + CELL_SIZE // 2) // CELL_SIZE
    row = (y - MARGIN + CELL_SIZE // 2) // CELL_SIZE

    # 판 범위를 벗어나지 않게 체크
    if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
        return row, col
    return None


def DrawStones(screen, omokpan):
    """돌 그리기"""
    from constants import MARGIN, CELL_SIZE

    for i in range(len(omokpan)):
        for j in range(len(omokpan[i])):
            if omokpan[i][j] != Stone.EMPTY:
                color = BLACK_COLOR if omokpan[i][j] == Stone.BLACK else WHITE_COLOR
                center = (MARGIN + j * CELL_SIZE, MARGIN + i * CELL_SIZE)
                pygame.draw.circle(screen, color, center, CELL_SIZE // 2 - 2)
