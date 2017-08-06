### dialogue under lovepoint 100

label waiting_100_01:

show kaede cafe_waiting_200_1

"뭐 해?"
#$persistent.love+=2
jump interaction


label waiting_100_02:

show kaede cafe_waiting_200_2

"심심하지 않아?"
#$persistent.love+=2
jump interaction


    
label c100_01:

show kaede cafe2_you_fucker

"난 기억하는데…. 진짜 너무해!"

#$persistent.love+=2

jump interaction




label c100_02:

show kaede cafe2_you_plz_rem

"아직도 나 기억 안나?"



#$persistent.love+=3


jump interaction




label c100_03:

show kaede cafe2_it_hurts_me

"으으, 다이어트는 너무 괴로워."

#$persistent.love+=3

jump interaction





label c100_04:

show kaede cafe2_iwanna_go

"놀러가고 싶다아"

#$persistent.love+=2
jump interaction

label c100_05:


show kaede cafe2_rem_by_you

"안 돼. 그런건 스스로 기억해내야지"


#$persistent.love+=2

jump interaction

label c100_06:

show kaede cafe2_happy_by_you

"오랜만에 만나서, 난 진짜 반가웠어!"

show kaede watsup


jump interaction

label c100_07:

show kaede cafe2_happy_by_you2

"날 만나러 온거야? 기쁜걸."


#$persistent.love+=2
jump interaction

label c100_08:

show kaede cafe2_wtf_asking
"응? 내 이름?"
show kaede cafe2_wtf_asking2
"흥, 안 알려줄거야!"

menu:
    "애교를 떤다":
        
        
        show kaede cafe2_wtf_done
        "......"
        "(......)"
        "............자살해"
        "(죽고싶다)"
    
    "알려주지 않으면 다시 오지 않겠다고 한다":
        show kaede cafe2_you_scum
        "정말 안올거야…..?"
        show kaede cafe2_you_scum_f
        "기억 못하는 네가 나쁜거잖아!"
    
    "제발 알려달라고 사정한다":
        show kaede cafe2_wtf_askingas
        "맨입으로 알려달라구?"
        "그냥 알려주기엔 너무 서운한걸!"


#$persistent.love+=2


jump interaction

label c100_09:

show kaede cafe2_infact

"그거 알고 있어? 사실 어릴 때 널 좋아했었어."

#$persistent.love+=2


jump interaction


label c100_10:

show kaede cafe2_cake

"달콤한 케이크가 먹고 싶어"

jump interaction