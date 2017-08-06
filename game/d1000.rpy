### dialogue under lovepoint 1000

label waiting_1000_01:

show kaede mu_whothink

"지금 뭐하는 거야? 누굴 생각하고 있어...?"

#$persistent.love+=2
jump interaction


label waiting_1000_02:

show kaede mu_plzwme

"날 보지 않는 넌 싫어."
#$persistent.love+=2
jump interaction




label waiting_1000_03:

show kaede mu_plzwme

"이젠 내가 싫어…..?"
#$persistent.love+=2
jump interaction


label waiting_1000_04:

show kaede mu_plzwme2

"나만 보라고 했는데... 왜 계속 다른 걸 보는거야?"
#$persistent.love+=2
jump interaction




label c1000_01:

show kaede mu_why_sad

"왜울어?"
"길냥이가 죽었다고? 얼마전에 새끼밴거?"
"(내가 그녀이에게 고양이가 죽은걸 말했었나?)"
show kaede mu_itsok
"괜찮아, 내가 있잖아? 난 항상 곁에 있어."
#$persistent.love+=2

jump interaction



label c1000_02:
show kaede mu_cantfor

"나 말고 다른 여자를 보는건 용서 할 수 없어."


#$persistent.love+=3


jump interaction




label c1000_03:


show kaede mu_igussno

"음? 알파카? 글쎄… 없어졌다는 거 같던데."
"왜인진 나도 모르지."

#$persistent.love+=3

jump interaction

label c1000_04:

show kaede mu_whyy

"벼룩시장을 연다더라. 이해가 안돼."
"어떻게 내껄 남한테 넘길 수가 있지?"
"나라면 차라리 넘길바에 없애버리겠어"

#$persistent.love+=2
jump interaction




label c1000_05:

show kaede mu_phonewhy

"왜 전화 안 받아?"

menu:
    "1. 새벽 두시면 자고있는게 당연하잖아…":
        show kaede mu_phonewhy_delta_1
        "거짓말… 솔직히 불어. 뭐하느라 안 받은거야?"
        "딴 년이랑 같이 있던건 아니겠지?"
    "2. 다음부터는 꼭 받을게":
        show kaede mu_phonewhy_delta_2
        "꼭 받아줘. 안 받으면 불안하다고."



#$persistent.love+=2

jump interaction

label c1000_06:


show kaede mu_phonewhy2

"넌 나만 알면 돼"

jump interaction

label c1000_07:

show kaede mu_knowhat

"스톡홀름 신드롬이라고 알아?"
"인질이 강도에게 반하는 현상이래."
show kaede mu_knowhat2
"어쩐지 로맨틱하지 않아?"


#$persistent.love+=2
jump interaction

label c1000_08:

show kaede mu_u_mine

"넌 내꺼야. 영원히."

menu:
    "1. 묘하게 로맨틱하다":
        "왠일이야? 간만에 막 머리를 쓰다듬구"
    "2. 어쩐지 오싹하다…":
        "왜 그런 표정이야…?"

#$persistent.love+=2


jump interaction

label c1000_09:

show kaede mu_u_so


"날 좋아하지 않아도 괜찮아. 내가 널 좋아하니까."
show kaede mu_u_so2
"……좋아하지 않더라도 계속 같이 있을 거야."



#$persistent.love+=2


jump interaction

label c1000_10:


show kaede mu_whowas
"누구랑 같이 있었어? 여자야?"

#$persistent.love+=2


jump interaction



label c1000_11:

show kaede mu_muse

"박물관을 다녀왔는데, 박제 체험이 제일 재밌더라."
"좀 더 큰 걸 해보고 싶어서, 제대로 배워 보려고. "

#$persistent.love+=2


jump interaction




label c1000_12:
show kaede mu_whowas

"그 남잔 누구야?"
show kaede mu_whowas2
"오늘 아침에 길에서 웬 남자랑 얘기했잖아."
"모르는 남자? 모르는 남자랑 왜 대화를 해?"
show kaede mu_dontlie
"길을 물었다고? 요즘 세상에? 대박. 거짓말 마. 그걸 어떻게 믿어?"

#$persistent.love+=2


jump interaction




label c1000_13:

show kaede mu_wnkillmom

"지하실을 내가 좀 쓰려고 하는데… 엄마가 방해해…"

#$persistent.love+=2


jump interaction





label c1000_14:

show kaede mu_p_chnage
"폰 패턴을 바꿨네. 왜 바꿨어?"
"나한테 숨겨야 할 내용이라도 있는거야?"

#$persistent.love+=2


jump interaction

label c1000_15:

show kaede mu_hon

"내것을 탐내는 것들에겐 교육이 필요해."
#$persistent.love+=2


jump interaction





label c1000_16:

show kaede mu_friend

"친구…? 그런거 필요 없어. 난 너만 있으면 돼."
show kaede mu_friend2
"너한테도 나만 있으면 되잖아. 그치?" 
show kaede mu_friend3

"…아냐?"

#$persistent.love+=2


jump interaction




label c1000_17:

show kaede mu_dontmeat

"내가 있는데 왜 딴 사람을 만나는거야?"

#$persistent.love+=2


jump interaction



label c1000_18:

show kaede mu_whyhateme

"나는 널 이렇게나 사랑하는데. 넌 왜 몰라주는 걸까?"
#$persistent.love+=2


jump interaction



label c1000_19:

show kaede mu_killmom

"드디어 그곳을 물려받게 됐어."
show kaede mu_killmom2
"엄마한텐 미안하지만... 어쩔 수 없었어."
show kaede mu_killmom
"넌 날 이해해 줄거지?"

#$persistent.love+=2


jump interaction

label c1000_20:

show kaede mu_no_sd

"수면제가 다 떨어졌네….."

#$persistent.love+=2


jump interaction



label c1000_21:

show kaede mu_ffudt

"요즘은 보라색보다도 붉은색이 더 좋은거 같아."
show kaede mu_killmom
"짙어지는 색을 보면... 마음이 안정되."
#$persistent.love+=2


jump interaction


label c1000_22:

show kaede mu_lazer1

"있잖아, 이마의 흉터…. 지우지 않을래?"
show kaede mu_lazer2
"불쾌하단 말야."
"다른년의 흔적이라니... 기분나빠"

jump interaction



label c1000_23:

show kaede mu_saw

"또 이가 나갔네… 톱날 손질하는 법좀 가르쳐 줄레?"

#$persistent.love+=2


jump interaction



label c1000_24:

show kaede mu_notmine

"아, 이거? 괜찮아, 내 피 아냐. 언제 묻은거지…"

#$persistent.love+=2


jump interaction



label c1000_25:

show kaede mu_notmine

"실종? 누가?"
show kaede mu_lost
"아, 지난번에 너랑 우리 가게 왔던 여자…."
"그런 여자 아무래도 상관 없잖아."

#$persistent.love+=2


jump interaction



label c1000_26:

show kaede mu_saw

"입을 막으면 침을 질질 흘려서 더러워."
"그렇다고 안 막으면 꺅꺅 시끄럽고."
"재갈이라도 사야 하나."

#$persistent.love+=2


jump interaction



label c1000_27:

show kaede mu_needmore

"그냥 죽이는 건 너무 자비로운거 같아."
"뭔가 더 고통스러운 방법이 없을까…"

#$persistent.love+=2


jump interaction


label c1000_28:

show kaede mu_notmine

"사람 몸에는 지방이 엄청 많더라."

#$persistent.love+=2


jump interaction


label c1000_29:

show kaede mu_notmine

"그거 알아? 사람은 죽을 때 온갖 체액이 흘러나와"
"그래서 나올 게 없을 때까지 굶겨야해."
show kaede mu_needmore
"안그럼 나중에 냄새도 고약하고, 뒷처리도 귀찮거든."

#$persistent.love+=2


jump interaction


label c1000_30:

show kaede mu_lost

"여우같은 게 내가 없는 새 지하실벽을 긁어놨어."
"얼마나 멍청하면 벽을 긁어서 나갈 생각을 했을까?"

#$persistent.love+=2


jump interaction


label c1000_31:

show kaede mu_lost

"잘못을 했으면 벌은 받아야 하는 거 아냐?"
"근데 벌 받기 싫다고 죽어버렸지 뭐야."
"너무 괘씸해서 갈아버렸는데도 분이 안풀려."
#$persistent.love+=2


jump interaction



label c1000_32:

show kaede mu_killgac

"창가 자리의 저 사람, 요즘 자꾸 널 훔쳐봐."
"…뽑아버려야 하나."

#$persistent.love+=2


jump interaction


label c1000_33:

show kaede mu_bibi

"나한테서 비린내가 나? 곤란하네…"
show kaede mu_bibi2
"어떻게 하면 안 튀게 처리할 수 있을까."

#$persistent.love+=2


jump interaction



#NEED HERE


label c1000_34:

show kaede mu_lost

"나한테서 널 뺏어가는건 뭐가 됐든 용서 못 해."

#$persistent.love+=2


jump interaction







label c1000_35:

show kaede mu_phonewhy_delta_3

"어떻게 붙잡아 두지….?"
"아이가 있다면..."

#$persistent.love+=2


jump interaction






label c1000_36:

show kaede mu_phonewhy_delta_4

"반장이 연락이 안 된다고…?"
"장난해? 아직도 걔랑 연락하고 있었단 말야?"
"내가 분명 하지 말라고 했을텐데…!"

#$persistent.love+=2


jump interaction

label c1000_37:

show kaede mu_phonewhy_delta_3

"(최근 신애가 차가운 눈을 할때가 있다)"
"(처음보는 눈빛인데도 묘하게 낯이 익다)"
"(무언가 떠오를듯 말듯…)"

#$persistent.love+=2


jump interaction



label c1000_38:

show kaede mu_phonewhy_delta_3

"(요즘들어 신애가 이상하다…)"

menu:
    "1. 헤어져야 하나…?":
        "..."

    "2. 그래도 신애는 여전히 사랑스럽다":
        "..."

    "3. 모르겠다. 슬슬 지쳐간다.":
        "..."


#$persistent.love+=2


jump interaction


