import pygame
from constants import WINDOW_SIZE, Stone
from core.board import OmokGame
from ui.render import DrawBoard, GetBoardPos, DrawStones


def main():
    # 1. 초기화
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))  # 현재 정사각형
    pygame.display.set_caption("⚪⚫Python Omok Game⚫⚪")
    clock = pygame.time.Clock()

    # 2. 게임 객체 생성 (상태 관리)
    game = OmokGame()

    running = True
    while running:
        # --- 이벤트 처리 (Input) ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # 클릭 좌표를 바둑판 인덱스로 변환
                pos = GetBoardPos(event.pos)

                if pos:
                    row, col = pos
                    # 클릭된 위치에 돌이 없을 경우 판정 진행
                    if game.omokpan[row][col] == Stone.EMPTY:
                        game.omokpan[row][col] = game.currentPlayer

                        # TODO: 여기서 판정 로직(CheckWin) 호출
                        print(f"[{game.currentPlayer.name}] ({row}, {col}) 착수")

                        # 턴 교체
                        game.SwitchPlayer()

        # --- 화면 그리기 (Output) ---
        # 1) 배경과 바둑판 선 그리기
        DrawBoard(screen)

        # 2) omokpan 배열을 돌며 실제 돌 그리기
        DrawStones(screen, game.omokpan)

        pygame.display.flip()
        clock.tick(60)  # 60 FPS 유지

    pygame.quit()


if __name__ == "__main__":
    main()
