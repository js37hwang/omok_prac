# ⚪⚫ Omoku Engine: Python & AI Project

객체지향 기반 오목 게임 프로젝트입니다.
Pygame을 활용한 로컬 대전부터 시작하여, 향후 강화학습 AI 연동 및 React 기반 웹 서비스 확장을 목표로 합니다.

---

## 🛠 Tech Stack

* **Language**

  * Python 3.12.10

* **Library**

  * `pygame`: 게임 엔진 및 GUI 구현
  * `socket`: 동일 네트워크 내 1:1 대전 (예정)
  * `PyInstaller`: 실행 파일(.exe) 배포

* **Tools**

  * VS Code/ WebStorm
  * Google Colab (AI 로직 테스트용)

---

## 📅 Development Log (Update History)

| 날짜         | 업데이트 내용                    | 비고           |
| ---------- | -------------------------- | ------------ |
| 2026-03-28 | 프로젝트 초기 설정 및 pygame 환경 구축  | -            |
| 2026-03-30 | 오목판 렌더링 및 기본적인 돌 놓기 로직 구현  | -            |
| 2026-04-01 | 승리 판정 알고리즘 및 렌주룰(6목 제한) 적용 | 가로/세로/대각선 검사 |
| 2026-04-03 | 함수 모듈화 및 리드미 작성            | 코드 리팩토링 진행   |
| Upcoming   | AI(강화학습) 연동 및 네트워크 모드 추가   | 진행 예정        |

---

## 📂 Directory Structure

```plaintext
gomoku-project/
├── data/                # [NEW] AI 학습 데이터 및 모델 파일
│   ├── models/          # 학습된 AI 모델 (.pth 또는 .h5)
│   └── replays/         # 게임 기보 저장용 (JSON/SQLite)
├── src/                 # 실제 소스 코드 (Source)
│   ├── main.py          # 게임 엔트리 포인트 (실행 파일)
│   ├── constants.py     # 설정값: 상수 (판 크기, 색상 RGB, 금수 규칙 등)
│   ├── core/            # [핵심] 게임 엔진 로직
│   │   ├── board.py     # 바둑판 배열 관리 (2차원 리스트)
│   │   ├── judge.py     # 승리 판정, 6목/3-3 금수 로직
│   │   └── player.py    # 사람/AI 플레이어 객체 정의
│   ├── ui/              # [그래픽] 화면 출력 관련
│   │   ├── assets.py    # 이미지/사운드 로드 관리
│   │   └── screen.py    # Pygame 화면 드로잉 함수
│   └── network/         # [네트워크] 통신 관련
│       └── socket_mgr.py # 서버/클라이언트 소켓 관리
├── assets/              # 리소스 파일
│   ├── images/          # 바둑판, 돌 이미지 (.png)
│   └── sounds/          # 착수음, 배경음 (.wav)
├── tests/               # 테스트 코드 (로직 검증용)
│   └── test_judge.py    # 승리 판정이 정확한지 테스트
├── requirements.txt     # 설치 필요한 라이브러리 목록
└── README.md            # 프로젝트 설명서
```

---

## 🚀 Key Features

* **정통 렌주룰 적용**

  * 흑의 3-3 금수 및 6목 승리 제한 로직 구현

* **효율적 알고리즘**

  * 전수 조사 방식이 아닌 *최근 착수 지점 기반 8방향 탐색*

* **모듈화 설계**

  * UI와 로직을 분리하여 추후 React 웹 버전으로 확장 용이

* **확장성**

  * 동일 네트워크 내 소켓 통신을 통한 실시간 대전 지원 예정

---

## 🕹 How to Run

### 1️⃣ 라이브러리 설치

```bash
pip install pygame
```

### 2️⃣ 게임 실행

```bash
python src/main.py
```

---

## 🔗 Roadmap & Future Work

* [ ] **AI Battle**

  * 강화학습 모델 기반 인공지능 대전 모드

* [ ] **Web Integration**

  * React + FastAPI 기반 브라우저 실행 버전

* [ ] **Ranking System**

  * SQLite 기반 승률 및 게임 시간 랭킹 시스템

---

#### commit convention

| Type     | Description                          | Example                                      |
|----------|--------------------------------------|----------------------------------------------|
| feat     | 새로운 기능 추가                     | feat: 오목 승리 판정 알고리즘 구현           |
| fix      | 버그 수정                            | fix: 돌이 겹쳐서 놓이는 오류 수정            |
| docs     | 문서 수정 (README, 주석 등)          | docs: 설치 및 실행 방법 업데이트             |
| style    | 코드 포맷팅 (로직 변경 없음)         | style: 들여쓰기 수정 및 세미콜론 추가        |
| refactor | 코드 리팩토링                        | refactor: 중복된 보드 그리기 로직 함수화     |
| test     | 테스트 코드 추가 및 수정             | test: 승리 조건 유닛 테스트 추가             |
| chore    | 빌드 업무, 패키지 설정, 가상환경     | chore: .gitignore에 .omok 폴더 추가          |
| rename   | 파일 혹은 폴더명 수정/이동           | rename: utils.py를 core/helper.py로 이동     |
| remove   | 파일 삭제                            | remove: 사용하지 않는 이미지 자산 삭제       |
| comment  | 주석 추가 및 변경                    | comment: 주요 함수 설명 주석 추가            |
