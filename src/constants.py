from enum import Enum
from enum import IntEnum


BOARD_SIZE = 19  # 오목판 칸 개수
MARGIN = 40  # 여백
CELL_SIZE = 30  # 칸 크기
BOARD_WIDTH = (BOARD_SIZE - 1) * CELL_SIZE  # 오목판 넓이
WINDOW_SIZE = BOARD_WIDTH + (MARGIN * 2)  # 화면 크기
WOOD_COLOR = (205, 133, 63)  # 오목판 색상
WHITE_COLOR = (255, 255, 255)  # 백돌 색상
BLACK_COLOR = (0, 0, 0)  # 흑돌 색상


# 흑돌/ 백돌
class Stone(IntEnum):
    BLACK = 1  # 검은돌: 1
    WHITE = -1  # 흰돌: -1
    EMPTY = 0  # 바둑판 reset용


# 오목/육목/삼삼 판정 돌 개수
class JudgeNum(IntEnum):
    OVER_LINE = 6
    OMOK_WIN = 5
    SAM_SAM = 3


# 판정 방향
class JudgeDirection(Enum):
    가로 = "horizontal"
    세로 = "vertical"
    슬 = "diag1"
    역슬 = "diag2"
