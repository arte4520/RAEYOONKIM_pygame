# RAEYOONKIM_pygame

             본 README는 python 언어가 설치되었다는 가정 하에,
             pygame을 처음 접하는 사용자들을 대상으로 작성되었습니다.


**준비사항**

            1) 명령어 프롬프트(Window 기준)에서 
               'pip install pygame' 을 입력해 pygame을 설치해주세요.

            2) 'crabs on the beach.py'파일은 실행파일이고, 
               이 디렉토리에 있는 모든 파일들은 실행에 꼭 필요한 파일들입니다.
               모든 파일을 한꺼번에 한 디렉토리 안에 다운로드 해주세요.

            3) 정상 실행 시, 바닷가 소리와 겹쳐서 잔잔한 음악이 담긴 노래가 함께 나옵니다.
                원본 음원의 소리가 매우 큰 관계로, default 사운드 볼륨을 많이 낮췄습니다.
                게임 시작 전에 다음과 같이 볼륨을 조정하시면 좋을 것 같습니다.
                
                         - 스피커를 사용 중일 경우 : 사운드 볼륨을 50% 이상으로 키우시는 것을 추천합니다.
                         - 이어폰을 사용 중일 경우 : 사운드 볼륨을 40% 이하로 줄이시는 것을 추천합니다.
                                     (그저 추천일 뿐이니, 적당히 기호에 맞게 조정하시면 됩니다)

**실행 권장사항 및 게임 '파일' 실행 방법**
          
            - 본 게임은 'IDLE (Python 3.8 32-bit)' 프로그램으로 제작과 시연을 완료했습니다.
              따라서, IDLE (Python 3.8 32-bit)을 통한 실행 권장사항만을 안내합니다.             
              (타 프로그램 이용 시 개별 구글링 결과를 참고해주세요.)
                            
                        1) 사용 중인 OS(운영체제) 내의 탐색기 검색창에 'IDLE'을 검색합니다.
                        2) 'IDLE (Python 3.8 32-bit)'을 실행합니다. (버전이 다를 수 있지만 보통은 괜찮습니다)
                        3) [File] 메뉴의 [Open]을 클릭 후, 파일을 다운받은 경로로 이동합니다.
                        4) 'crabs on the beach.py' 파일을 선택 후 열어주세요.
                        5) 키보드에서 [F5] 키를 누르면 게임이 시작됩니다.


**게임규칙**

             - 화면을 정면으로 보는 유저의 시각에서,
               왼편에 있는 크랩이 '유저의 크랩', 오른편에 있는 크랩이 '컴퓨터의 크랩'입니다.

             - 오른쪽 크랩은 자동으로 움직입니다.
             
             - 왼쪽 크랩은 유저의 마우스를 따라 움직입니다.
             
             - 크랩에 부딪힌 공은 튕겨져 나가고,
               게임 스크린 엣지에 부딪혀 반대편 크랩으로 향합니다.

             - 왼쪽 스크린 엣지 밖으로 공이 넘어가면, 오른쪽 크랩(컴퓨터)이 1점을 획득합니다.
               (유저의 진영)

             - 오른쪽 스크린 엣지 밖으로 공이 넘어가면, 왼쪽 크랩(유저)이 1점을 획득합니다.
               (컴퓨터의 진영)
            
             - 왼쪽 크랩(유저)과 오른쪽 크랩(컴퓨터) 중 4점을 먼저 얻는 편이 승리합니다.
             
             - 왼쪽 크랩(유저)이 1점을 획득할 때마다, 
               화면 중앙에는 STAGE 1, STAGE 2, STAGE 3, LAST STAGE가 차례로 표시됩니다.
               
             - STAGE 단계가 높아질 때마다, 게임의 난이도가 높아집니다.
               
             - 오른쪽 크랩(컴퓨터)이 1점을 획득할 때에는 STAGE 단계가 변화하지 않습니다.
               (= 오른쪽 크랩(컴퓨터)만 득점하면 게임의 난이도는 높아지지 않습니다)
               
                  
**게임방법**

            1) 'crabs on the beach.py' 파일을 열어, 게임을 실행합니다.

            2) 'Crabs on the beach'
               'Press the space bar' 라는 문구가 뜨면 초기 화면으로 진입된 것입니다.
                                     해당 화면에서 [space bar]를 누릅니다.

            3) 게임이 시작되면, 크랩들이 테니스공으로 핑퐁 게임을 합니다.

            4) 왼쪽 크랩은 마우스를 따라 움직입니다.
               왼쪽 크랩을 이용해, 공이 왼쪽 스크린 밖으로 나가지 않게 막아주세요!

            5) 왼쪽 크랩이 4점을 먼저 얻게 되면 승리하고,
               오른쪽 크랩이 4점을 먼저 얻게 되면 패배합니다.

            6) 게임이 종료되면 승패 결과가 "WIN"과 "LOSE"로 화면의 중앙에 나타납니다.

            7) 게임을 또 하고 싶다면, 
               승패 결과 화면에서 [space bar]를 다시 눌러주세요.
