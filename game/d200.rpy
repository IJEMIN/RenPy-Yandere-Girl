### dialogue under lovepoint 200

label waiting_200_01:

show kaede th_wuthink

"무슨 생각해?"
#$persistent.love+=2
jump interaction


label waiting_200_02:

show kaede th_hey_there

"저기요? 똑똑똑?"
#$persistent.love+=2
jump interaction


    
label c200_01:
show kaede third_happy_seeya
"널 다시 만나서 다행이야, 헤헷."

#$persistent.love+=2

jump interaction

label c200_02:

show kaede th_simsim

"우~우! 심심해!"


#$persistent.love+=2


jump interaction




label c200_03:
"넌 뭐 할 얘기 없어?"

show kaede th_gimmetalk

#$persistent.love+=2

jump interaction

label c200_04:

show kaede th_how_holi

"다음 주말에 어디 놀러갈까?"

#$persistent.love+=2
jump interaction

label c200_05:

show kaede th_got_gf

"그동안 여자친구 없었어? 응? 응?"
menu:
    "없었다":
        show kaede th_got_gfhh
        "정말?"
        show kaede th_got_gfhhrr
        "정말정말정말?"
    "없었다":
        show kaede th_got_gflie
        "에이, 거짓말"
        show kaede th_got_gflierr
        "...진짜야?"



jump interaction

label c200_06:

show kaede th_how_togetlv
"사랑은 쟁취하는 거지!"

#$persistent.love+=2


jump interaction

label c200_07:


show kaede th_nxtdoor

"옆집에 미소년이 이사를 왔대."

show kaede th_nxtdoorhmdub

"이름이 제민….?(설명충: 제작자 이름이다. 현실 미소년임)"

#$persistent.love+=2


jump interaction


label c200_08:


show kaede th_iwaumore

"좀 더 자주 와줬으면 좋겠어."

#$persistent.love+=3


jump interaction

label c200_09:


show kaede th_loli

"개발자가 로리콘이래. …….근데 로리콘이 뭐야?"

#$persistent.love+=2


jump interaction

label c200_10:

scene bg_room

show kaede temp_swim_how at center

with dissolve

"으으으으음….! 이렇게? 아냐, 이게 더...?"
"(신애가 거울을 보면서 이상한 포즈를 취한다. 뭐하는거지…?)"

show kaede temp_swim_suprise

"엄마야! 기척도 없이 오면 어떡해!"

#$persistent.love+=3


scene bg_uptown 
show kaede th_love_chicken at center
with dissolve

jump interaction



label c200_11:

show kaede th_love_swarm

"난 안개낀 날이 좋아. 뭔가 오싹 하지 않아?"

#$persistent.love+=2

jump interaction




label c200_12:

show kaede th_movie_ar

"액션영화에서 악당들이 지는 건 너무 물러터져서 그런걸거야."
show kaede th_movie_ar2

"기껏 인질을 잡아놓고 죽일거라고 큰소리만 쳐대다니, 겁이라도 먹은 걸까?"

show kaede th_movie_ar3

"그러니 그냥 호구취급이나 당하는거지."

#$persistent.love+=2

jump interaction

label c200_13:
scene bg_room
show kaede th_love_chicken at center
with dissolve

"역시 치킨은 파닭이 최고야"

#$persistent.love+=2
scene bg_uptown 
show kaede th_love_chicken at center
with dissolve
jump interaction

label c200_14:

show kaede th_gogo_beach

"바다 가자, 바다! 가자아~ 응?"

menu:
    "1. 바빠서 무리야":
        show kaede d_200_beach
        "아 그래…"
    "2. 그래 가자!":
        show kaede d_200_beach2
        "꺄! 고마워!"
        "예쁜거 입을테니까 너도 멋지게 하고 와!"

#$persistent.love+=3

jump interaction


label c200_15:

show kaede th_loveu

"저기.., 널 좋아하는 것 같아."

#$persistent.love+=3

jump interaction



label c200_16:

show kaede d_200_beach
"옛날 일은 잘 기억이 안난다고?"
"그 사고 때문인가…"
show kaede d_200_16
"졸업날 전에 계단에서 굴렀잖아. 이마에 상처도 그 때 난거구."
"기억 안 나?"
"(사고…? 아무리 생각해봐도 잘 모르겠다)"
show kaede d_200_16_2
"안나나 보네. 졸업식도 못와서 얼마나 서운했는데."

#$persistent.love+=3

jump interaction


label c200_17:

show kaede d_200_16_2

"좀 더 같이 지내고 싶었는데…"
"졸업하고 너네 집이 이사를 가버려서..."
show kaede d_200_17
"이제라도 다시 만나서 다행이야!"
show kaede d_200_17_2
"이렇게 만난걸 보면… 운명?!"
"아하하, 농담이야."

#$persistent.love+=3

jump interaction


label c200_18:
show kaede d_200_18
"감동적이었어… 담에 또 같이 영화보자!"

#$persistent.love+=3

jump interaction