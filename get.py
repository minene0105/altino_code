import requests

### 김승준 선생님의 서버로 GET 요청을 날리는 함수 ###

## ! 첫번째 인자는 이름, 두번째 인자는 전화번호, 세번째 인자는 시간을 입력하면 됩니다 ! ##
## ! 인자에 들어가는 변수 값 모두 자료형은 상관 없습니다 ! ##

def recordUserData( UserName, UserPhone, UserScore ) :
    requests.get('http://desk.sjkim.net:8888/score?NAME=' + str( UserName ) + '&PHONE=' + str( UserPhone ) + '&SCORE=' + str( UserScore ))
    print(str(UserName) + "님의 정보 등록이 완료 되었습니다.")

recordUserData("짜장면사줘", "짜장면먹고싶다사주세요", 0.01)
