label waiting_050_01:

show kaede cafe_waiting

"같이 대화 좀 해주세요."
#$persistent.love+=2
jump interaction


label waiting_050_02:

show kaede cafe_waiting2

"말주변이 별로 없으신가봐요."
#$persistent.love+=2
jump interaction


    
label c050_01:

show kaede cafe_again
"또 오셨네요?"
show kaede cafe_ok
"카페라떼 한 잔, 맞죠? 헤헤"

#$persistent.love+=2

jump interaction

label c050_02:

show kaede cafe_quetion

"혹시, 전에 저랑 만난 적이 있으신가요?"

#$persistent.love+=3

jump interaction

label c050_03:

show kaede cafe_curious

"이상하다… 분명 어디선가 본거 같은데…"
#$persistent.love+=3

jump interaction

label c050_04:

show kaede cafe_smile

"오늘은 날이 좋네요."

#$persistent.love+=2
jump interaction

label c050_05:

show kaede succeding_mom

"여기는 어머니가 하시는 카페에요."

show kaede succeding_mom_smile


"나중에 제가 여길 물려받을 거에요!"
#$persistent.love+=2

jump interaction

label c050_06:

show kaede watsup

"무슨 일 있으셨어요?"

#$persistent.love+=2
jump interaction

label c050_07:

show kaede night_scary

"밤에는 이상한 손님들이 있어서 무서워요."

#$persistent.love+=2
jump interaction

label c050_08:

show kaede anger

"제발 카페에서 기저귀는 안 갈았으면 좋겠어."
#$persistent.love+=2
jump interaction

label c050_09:

show kaede pretty_good

"손님은 눈이 참 예쁘세요."
#$persistent.love+=3
jump interaction


################
