# src/constants.py
from constants import BOARD_SIZE, Stone


class OmokGame:
    def __init__(self):
        """
        게임 초기화
        1 오목판 초기화
        2 사용자 초기화
        """
        self.omokpan = []
        self.currentPlayer = Stone.BLACK.value

        for i in range(Stone.EMPTY.value, BOARD_SIZE):
            temp = []
            for j in range(Stone.EMPTY.value, BOARD_SIZE):
                temp.append(Stone.EMPTY.value)

            self.omokpan.append(temp)

        self.currentPlayer = Stone.BLACK.value

    def SwitchPlayer(self):
        """
        플레이어 교체
        """
        # 플레이어 교체
        self.currentPlayer = (
            Stone.WHITE.value
            if self.currentPlayer == Stone.BLACK.value
            else Stone.BLACK.value
        )
