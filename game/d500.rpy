### dialogue under lovepoint 500

label waiting_500_01:

show kaede sc_mylover

"자기야♡"
#$persistent.love+=2
jump interaction


label waiting_500_02:

show kaede sc_gimmeat

"나한테도 신경 좀 써줘!"
#$persistent.love+=2
jump interaction




label waiting_500_03:

show kaede sc_nope

"권태기인가…"
#$persistent.love+=2
jump interaction






label c500_01:

show kaede sc_livewithu

"세상에 너랑 나랑 둘만 남았으면 좋겠어"
#$persistent.love+=2

jump interaction



label c500_02:
show kaede sc_onlyu

"난 너만 있으면 돼"


#$persistent.love+=3


jump interaction




label c500_03:


show kaede sc_plzfme

"오늘 우리 집에 아무도 없는데…… 커피 마시고 갈래...?"

#$persistent.love+=3

jump interaction

label c500_04:

show kaede sc_myhurt

"니가 다른 사람이랑 있으면 가슴이 아파"

#$persistent.love+=2
jump interaction

label c500_05:

show kaede sc_udo

"난 너랑 하는거면 뭐든 다 좋아!"


#$persistent.love+=2

jump interaction

label c500_06:


show kaede sc_justHappy

"할 말이 없어… 그래도 너랑 있어서 좋다!"

jump interaction

label c500_07:

show kaede sc_tellmefav

"있잖아, 어떤 타입이 좋아?"
show kaede sc_tellmefav2
"나 같은 타입? 아니면……"
show kaede sc_tellmefav3
"나 같은 타입?"


#$persistent.love+=2
jump interaction

label c500_08:

show kaede sc_catyo

"어제 집 근처에서 길고양이랑 놀고 있더라?"

show kaede sc_catyosex
"고양이말고 나랑도 놀아줘!"


#$persistent.love+=2


jump interaction

label c500_09:

show kaede sc_near_hear


"요 근처 학교에서 알파카를 키운대."

show kaede sc_near_hear2
"근데 그런데서 키울 수가 있나?"
show kaede sc_near_hear3
"….뭐? 그런게 보고 싶어? 그게 그렇게 좋아?"


#$persistent.love+=2


jump interaction

label c500_10:


show kaede sc_shyshy
"이, 이거 언제까지 해야해? 좀 부끄러운데…"

#$persistent.love+=2


jump interaction



label c500_11:

show kaede sc_pastsor

"우리 어릴 때 담임 쌤, 다음 달에 결혼 하신대. 부럽다…."

#$persistent.love+=2


jump interaction




label c500_12:
show kaede sc_hansome

"이렇게 보면 꽤 잘생긴 것도 같고…. 콩깍지인가?"

#$persistent.love+=2


jump interaction




label c500_13:

show kaede sc_gawan

"관람차야 말로 데이트의 꽃 아냐?"

show kaede sc_gawan2

"10분동안 단 둘이라니, 두근거려."

#$persistent.love+=2


jump interaction





label c500_14:

show kaede sc_neet
"이미 아무것도 안하고 있지만…"
"더욱 격렬하게 아무것도 안하고 싶다….."

#$persistent.love+=2


jump interaction

label c500_15:

show kaede sc_ucome

"보고 싶다고 생각했더니 니가 왔어!"
"우리 뭔가 통하는 것 같지 않아?"

#$persistent.love+=2


jump interaction





label c500_16:

show kaede sc_mkloveme

"날 좋아하지 않으면 날 좋아하게 만들면 되지."

#$persistent.love+=2


jump interaction




label c500_17:

show kaede sc_mkloveme

"네가 나만 바라보면 좋겠어."

#$persistent.love+=2


jump interaction



label c500_18:

show kaede sc_yester

"어제 장을 보러 가는데, 대박 음험해보이는 사람이 말을 걸더라?"
"나이스 보트 어쩌고 중얼거리다 가버렸어"
show kaede sc_wtisboat
"...미친걸까? 대체 배가 뭘 어쨌다는 걸까."

#$persistent.love+=2


jump interaction



label c500_19:

show kaede sc_loveusomuch

"내가 너 정말 좋아하는거 알지?"

#$persistent.love+=2


jump interaction

label c500_20:

show kaede sc_100

"100일 선물은 커플링이 좋겠어."

show kaede sc_1002
"서로 선물하는 거야. 너는 나한테, 난 너한테. 결혼식처럼! 어때?"

#$persistent.love+=2


jump interaction



label c500_21:

show kaede sc_lvway

"사랑이란건 서로 같은 방향을 바라보는 거래."

#$persistent.love+=2


jump interaction


label c500_22:

show kaede sc_whothatgirl

"그 여잔 누구야….?"
menu:
    "친한 선배야":
        show kaede sc_whothatgirl2
        "흐-음, 저런 여자랑….."
        #$persistent.end_lover +=1
    "그냥 아는 사람이야":
        show kaede sc_whothatgirl3
        #$persistent.end_killer +=1
        "그냥 아는 사람이랑 단 둘이 커피를 마신다고?"
        show kaede sc_whothatgirl4
        "그게 지금 말이 된다고 생각해?"
        show kaede sc_whothatgirl5
        "변명하지마!"
    "3. 너랑 별 상관없잖아?":
        show kaede sc_whothatgirl6
        "왜 그런 말을 하는거야….?"    


#$persistent.love+=2


jump interaction










#NEED HERE




label c500_22:

show kaede sex_is_tiring

"너무 격렬한건 피곤해"

#$persistent.love+=2


jump interaction




label c500_23:

show kaede so_me

"나 어때?"
show kaede so_see_me
"뭐, 뭐야? 왜 그렇게 뚫어져라 보는거야? 변태!"
show kaede so_u_likeit
"……저기, 그래서… 맘엔 들어?"

menu:
    "1. 예쁘다고 해준다":
        show kaede so_500_23_1
        "당연하지!"
        "다이어트하느라 얼마나 고생했는데."
    "2. 뺨에 뽀뽀해준다":
        show kaede so_500_23_2
        "바, 밖에서 뭐하는거야!"
        "…. 한 번 더 해줘."
    "3. 더 빼야겠다고 한다":
        scene black with fade
        "짝!"
        "(헐. 나 지금 뺨 맞은거?)"
        "됐어! 나 갈거야! 변태머저리! 죽어!"
        jump u_fucked_up



#$persistent.love+=2


jump interaction


label u_fucked_up:
"< BAD ENDING >"
python:
    persistent.game_cleared = True
    persistent.love = 0
    
    
    persistent.intro_cleared = False
    
    persistent.event050_cleared = False  
    persistent.event100_cleared = False
    
    persistent.location = "CAFE"
    
    persistent.cloth = "CAFE"
    persistent.event200_cleared = False
    persistent.event350_cleared = False
    persistent.event500_cleared = False
    persistent.event650_cleared = False
    persistent.event700_cleared = False
    
    persistent.ghost_love_pt = 0


$renpy.quit()



label c500_24:

show kaede u_home_500

"오늘은 언제 와?"

menu:
    "1. 오늘은 좀 바쁜데. 나중에 보자":
        show kaede u_home_500_2
        "설마 집에서 롤할거야?"
    "2. 오래는 못 있고… 잠깐 들렀다 갈게":
        show kaede u_home_500_3
        "응! 오면 내가 마사지 해줄게!"
        

#$persistent.love+=2


jump interaction


label c500_24:

show kaede u_home_500_4

"어? 웬 꽃이야? 나 주려고?"

menu:
    "1. 널 위한 거야":
        show kaede u_home_500_3
        "고마워! 기뻐!"
    "2. 받았어":
        show kaede u_home_500_5
        "꽃을…? 누구한테서…?"
        

#$persistent.love+=2


jump interaction



label c500_25:

show kaede sc_shyshy

"매일매일 널 보고 싶어"
        

#$persistent.love+=2


jump interaction
