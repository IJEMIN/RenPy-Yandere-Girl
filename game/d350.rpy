### dialogue under lovepoint 350

label waiting_350_01:

show kaede c5_think_me

"나 두고 딴 생각하지마"
#$persistent.love+=2
jump interaction


label waiting_350_02:

show kaede c5_hey_yo

"심심하게 냅두지 말아줄래?"
#$persistent.love+=2
jump interaction




label waiting_350_03:

show kaede c5_play_withme

"나랑 놀아줘"
#$persistent.love+=2
jump interaction
    





label c350_01:

show kaede c5_loveyaeye

"니 눈이 제일 좋아."
"특히 날 보고 있을 때."
#$persistent.love+=2

jump interaction



label c350_02:
show kaede c5_youreworld

"내겐 니가 전부야. 정말이라구?"


#$persistent.love+=3


jump interaction




label c350_03:


show kaede c5_lovelovelove

"좋아해 좋아해 좋아해!"

#$persistent.love+=3

jump interaction

label c350_04:

show kaede c5_color

"내가 좋아하는 색?"
"보라색인데, 왜?"

#$persistent.love+=2
jump interaction

label c350_05:

show kaede c5_change_allba

"알바생을 다 남자로 바꿔야겠어…"


#$persistent.love+=2

jump interaction

label c350_06:


show kaede c5_makeya_food

"먹고 싶은 거 있어? 내가 만들어줄게."


jump interaction

label c350_07:

show kaede c5_yumafate

"점을 쳐봤는데, 너랑 나랑 최고의 궁합이래!"


#$persistent.love+=2
jump interaction

label c350_08:

show kaede c5_gimatime

"널 기다릴 땐 시간이 너무 길어"


#$persistent.love+=2


jump interaction

label c350_09:

show kaede c5_foru

"짠, 널 위한 특별한 라떼 아트!"

show kaede c5_foru2

"하트 말고 다른 것도 만들 수는 있지만…."

show kaede c5_foru3
"이건 내 사랑의 표현이라고."

#$persistent.love+=2


jump interaction

label c350_10:


show kaede c5_allIneed
"난 너만 있으면 돼. 진짜야."

#$persistent.love+=2


jump interaction



label c350_11:

show kaede c5_notMaCur

"호러 영화? 무서운 건 아니지만… 별로 재미가 없는걸."

#$persistent.love+=2


jump interaction




label c350_12:
show kaede c5_wannasex

"쓰리사이즈는 비밀이야."

#$persistent.love+=2


jump interaction




label c350_13:

show kaede c5_poss

"니트족인데 아이돌이 될 수가 있는건가?"

#$persistent.love+=2


jump interaction





label c350_14:

show kaede c5_cumdate
"오늘은 나랑 데이트하자?"

#$persistent.love+=2


jump interaction

label c350_15:

show kaede c5_tellmeya

"넌 날 어떻게 생각해?"

#$persistent.love+=2


jump interaction







label c350_16:

show kaede d_c350_16
"비오네… 갑자기 옛날 생각난다."
"점심때 둘이서 몰래 학교 나갔다가 비 쫄딱 맞고 돌아왔지. "
show kaede d_c350_16_2
"담임한테 엄청 털렸잖아, 하하."

menu:
    "1. ….넌 왜 그런걸 기억하냐.":
        show kaede d_c350_16_3
        "누구랑 달라서 기억력이 좋거든."
        show kaede d_c350_16_4
        "아~ 옛날 기억나니까 좋다. 그치?"
    "2. 그랬나…? 기억 안나는데.":
        show kaede d_c350_16_5
        "그래? 그럼 기억나게 비라도 좀 맞아볼까?"
        "(…뭐?!)"
        scene bg_rain with vpunch
        "(신애가 내 손을 잡고 빗속으로 뛰쳐나갔다)"
        "아하하, 어때? 시원하지 않아?"
        
scene bg_cafe_day with dissolve
show kaede c5_cumdate at center with dissolve

#$persistent.love+=2


jump interaction





label c350_17:
show kaede d_c350_17_1
"케이크는 서비스랍니다, 손님!"
"딴 사람들한텐 비밀! 너한테 몰래 주는거야."

#$persistent.love+=2


jump interaction





label c350_18:
show kaede d_c350_18
"나 뭐 달라진거 없어?"

menu:
    "1. 잘 모르겠는데….?":
        show kaede d_c350_18_2
        "진짜 모르겠어? 너 나한테 관심이 별로 없구나?"
    "2. 살쪘냐?":
        show kaede d_c350_18_3
        "…나가 죽어"
    "3. 새 옷 샀어?":
        show kaede d_c350_18_4
        "정답! 예쁘지 않아? 물론 내가 말야."
    "4. 좀 더 예뻐진거 같다":
        show kaede d_c350_18_5
        "흥, 아부로 넘어갈 수 있을거 같냐!"
        show kaede d_c350_18_6
        "...…그런데.. 다시 한번 말해줄래?"

#$persistent.love+=2


jump interaction





label c350_19:

show kaede d_c350_19_1
"바다 가고 싶어. 같이 가 줄거지?"

menu:
    "1. 난 물이 싫은데…":
        show kaede d_c350_19_2
        "그러지 말고 가자, 응? 재밌을 거야!"
    "2. 네가 원한다면 가야지":
        show kaede d_c350_19_3
        "신난다! 자기 최고!"
        "(이런거라면 매일 가도 괜찮을지도…)"

#$persistent.love+=2


jump interaction