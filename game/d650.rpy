
### dialogue under lovepoint 650

label waiting_650_01:

show kaede its_650_w1

"날 두고 다른 생각하지마"
#$persistent.love+=2
jump interaction


label waiting_650_02:

show kaede its_650_w1

"뭐해…?"
#$persistent.love+=2
jump interaction




label waiting_650_03:

show kaede its_650_w1

"지금 뭐하는 거야? 누굴 생각하고 있어?"
#$persistent.love+=2
jump interaction






label c650_01:

show kaede its_650_01

"자꾸 그 얘기하면 화낼거야."
#$persistent.love+=2

jump interaction



label c650_02:
show kaede its_650_02

"나만 바라보면 좋겠어."


#$persistent.love+=3


jump interaction




label c650_03:


show kaede its_650_03

"어젠 왜 안왔어…?"
show kaede its_650_04
"아무리 바빠도 그렇지. 그게 나보다 소중해?"

#$persistent.love+=3

jump interaction

label c650_04:

show kaede its_650_05

"너 요즘 나한테 너무 소홀해"

#$persistent.love+=2
jump interaction

label c650_05:

show kaede its_650_06

"보고싶었어!"
menu:
    "1. 겨우 이틀인데…?":
        show kaede its_650_07
        "너무해…! \"이틀\"이라고!"
        "넌 내가 보고 싶지 않은 거야?"
    "2. 나도 보고싶었다고 한다":
        show kaede its_650_08
        "진짜? 진짜 너도 내가 보고싶었어?"


#$persistent.love+=2

jump interaction

label c650_06:


show kaede its_650_09

"너 없는 하루는 너무 길어."

jump interaction

label c650_07:

show kaede its_650_10

"(신애가 무서운 눈으로 생각에 잠겨 있다)"
show kaede its_650_08
"앗, 언제 왔어? 어서와!"
"(다가가자 해사하게 웃는다. 잘못 본건가…?)"


#$persistent.love+=2
jump interaction

label c650_08:

show kaede its_650_11

"다른 사람이랑 있는 널 보면 불안해... 참을 수 없어"


#$persistent.love+=2


jump interaction

label c650_09:

show kaede its_650_12


"아침에 보니까 누가 곰인형 큰거 버렸더라. 헤어졌나봐."
show kaede its_650_13
"...우린 괜찮겠지…?"


#$persistent.love+=2


jump interaction

label c650_10:


show kaede its_650_11
"내가 모르는 곳에 니가 있다고 생각하니... 무서워서 참을 수 없어"

#$persistent.love+=2


jump interaction



label c650_11:

show kaede its_650_08

"나랑 좀 더 있자."

#$persistent.love+=2


jump interaction




label c650_12:
show kaede its_650_14

"니가 나한테 잘해줄 때마다 진짜 행복해."
show kaede its_650_16
"근데 그만큼 무섭기도 해... 언젠가 끝이 날까봐"

#$persistent.love+=2


jump interaction




label c650_13:

show kaede its_650_08

"난 이제 너 없이는 못살것 같아."
#$persistent.love+=2


jump interaction



label c650_20:

show kaede its_650_16

"무서운 꿈을 꿨어…"
"변해버렸어. 변해버려서, 날 두고, 날 두고…!"
show kaede its_650_07
"…...항상 같은 모습으로 있어줄거지?"

#$persistent.love+=2


jump interaction





label c650_14:

show kaede its_650_08
"보고싶어 보고싶어 보고싶어"
"하루라도 떨어져 있고 싶지 않아"

#$persistent.love+=2


jump interaction

label c650_15:

show kaede its_650_08

"이틀에 한 번은 부족해. 매일 널 갖고 싶어."
#$persistent.love+=2


jump interaction





label c650_16:

show kaede its_650_17

"나만 바라봐줘. 나만 사랑해줘."
"제발…"

#$persistent.love+=2


jump interaction

label c650_17:

show kaede its_650_01

"동창회? 또 그 얘기야? 이미 싫다고 했잖아."
"난 반장 보고 싶지도 않고, 니가 걜 만나는 것도 싫어."
#$persistent.love+=2
jump interaction


label c650_18:

show kaede its_650_01

"떨어질 거면 혼자 떨어질 것이지."
"애먼 널 깔아뭉개는 바람에 너만 다쳤잖아!"
#$persistent.love+=2
jump interaction




label c650_19:

show kaede its_650_01

"니가 애들을 보고 싶어하는거 이상으로 난 가고 싶지 않아"
#$persistent.love+=2
jump interaction




