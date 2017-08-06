### Events on this scripts


label event_on_050:

show kaede cafe_are_you_ok

"어휴, 이 땀 좀 봐. 뛰어왔어요?"
"잠시만요, 닦아드릴게요."
"(...그린라이트?)"
"어..? 이마에 상처가......?! 그럼 손님은..!"

#$persistent.love+=3

show kaede cafe_would_you_remember

"저기, 기억 안 나요? 초등학교 때 같은 반이었는데....."

menu:
    "미안 모르겠어":
        show kaede cafe_wontRem
        "너무 어릴때라 그런가?"
        show kaede cafe_wontRem2
        "그래도 계속 보다보면 기억이 나겠지?"
        show kaede cafe_wontRem3
        "잘 생각해 봐!"
    "누군지는 모르겠지만, 일단은 오랜만이라며 웃는다.":
        show kaede cafe_wontRem4
        "거짓말. 기억 못하는 얼굴인데?"
        show kaede cafe_wontRem5
        "잘 생각해 보라구!"


$persistent.event050_cleared = True

jump interaction

label event_on_100:


show kaede cafe3_wyasking
"응? 내 이름?"
show kaede cafe3_wyasking_so
"너 진짜 끈질기다. 아직도 기억을 못 해냈단 말이야?"
show kaede cafe3_wyasking_so_yw
"어쩔까... 알려줄까, 말까"

menu:
    "이름 하나 알려주는데 되게 비싸게 구네":
        show kaede third_wtfsaid
        "지금 뭐라고 했어?"
        show kaede third_uworst
        "정말 최악이야!"
        #$persistent.love-=6
    "알려주면 너에 대해 기억해낼지도......":

        show kaede third_looksok
        "나름 일리는 있네…."
        show kaede third_looksok_tellya
        "좋아 그럼. 내가 인심 썼다!"

        show kaede third_looksok_maname
        "신애야, 내 이름."
        show kaede u_fish
        "뭐냐, 머리는 장식이야?"
        show kaede u_fish2
        "한학기 내내 너 옆자리였잖아. 학원도 같이 다녔거든!"

        menu:
            "기억이 날듯 말듯하다.":
                show kaede u_saw_mypants
                "멍청이! 내 속옷도 봐놓고서!"
                "(아..! 그 안경을쓴.. 음침녀!)"
                show kaede third_looksok_maname_dnt
                "…….안경 미소녀겠지?"
                "(분명 웃고 있는데 등골이 서늘하다. 여자란 무서워….)"
            "2-2. 앗! 하얀 곰돌이 속옷!":
                show kaede u_hentai12
                "이… 이 변태!"
                show kaede u_hentai123
                "기억에서 지워. 당장!"


    "알려주면 소원 하나 들어줄게":
        show kaede third_really
        "진짜?"
        show kaede third_really_really
        "약속한거지?"
        show kaede third_really_really_awe
        "꼭이야?"
        show kaede third_looksok_maname
        "신애야, 내 이름."
        show kaede u_fish
        "뭐냐, 머리는 장식이야?"
        show kaede u_fish2
        "한학기 내내 너 옆자리였잖아. 학원도 같이 다녔거든!"

        menu:
            "기억이 날듯 말듯하다.":
                show kaede u_saw_mypants
                "멍청이! 내 속옷도 봐놓고서!"
                "(아..! 그 안경을쓴.. 음침녀!)"
                show kaede third_looksok_maname_dnt
                "…….안경 미소녀겠지?"
                "(분명 웃고 있는데 등골이 서늘하다. 여자란 무서워….)"
            "2-2. 앗! 하얀 곰돌이 속옷!":
                show kaede u_hentai12
                "이… 이 변태!"
                show kaede u_hentai123
                "기억에서 지워. 당장!"



$persistent.event100_cleared = True

$persistent.location = "UPTOWN"
scene bg_uptown
show kaede third_happy_seeya at center
with dissolve
jump interaction





label event_on_200:
scene bg_cafe_day
show kaede c5_lovelovelove at center
with dissolve
"사랑해 사랑해 사랑해"
$persistent.event200_cleared = True

jump interaction






label event_on_350:



scene bg_school_out
show kaede sc_yo_past at center
with dissolve
"솔직히 말해봐. 정말 그동안 여자친구 없었어?"

menu:
    "없었다":
        show kaede sc_sns
        "아 그래? 요즘 페북 기능이 참 좋더라구."
        #$persistent.end_killed+=1
    "있었다":
        show kaede sc_from_hear
        "아 그래...? 뭐, 이제는 나만 보게 할거니까"
        show kaede sc_killafter
        "그런데 누구였어? 사진도 있어?"
        #$persistent.end_lover+=1


$persistent.event350_cleared = True

jump interaction


label event_on_500:


play music "Moonlight_Sonata_by_Beethoven.mp3"
scene bg_school_out
show kaede its_650_01 at center
with dissolve
"뭐? 동창회? 싫어!"
"나 반장 진짜 싫어한단 말야…"
show kaede its_650_16
"나 버리고 갈거야?"

menu:
    "1. 그럼 나 혼자 다녀올게":
        show kaede its_650_w1
        "아, 안돼! 싫어!"
        "넌 기억이 안난댔지만… 니 상처, 그 애 때문인걸."
        show kaede its_650_01
        "그 멍청이가 계단에서 떨어져가지고…!"
        show kaede its_650_08
        "가지마. 너 하고 싶은거 다 해줄게. 응?"

    "2. 아쉬운데…":
        show kaede its_650_08
        "안돼안돼. 그냥 나랑 있자."
        "내가 기분 좋게 해줄게."
        show kaede its_650_11
        "넌 기억이 안난댔지만… 니 상처, 그 애 때문인걸."
        show kaede its_650_01
        "그 멍청이가 계단에서 떨어져가지고…!"

    "3. 안갈테니 진정해":
        show kaede its_650_08
        "이해해주는구나! 오늘 찐한 서비스 해줄게!"

$persistent.event500_cleared = True

jump interaction


label event_on_650:

scene black
show kaede its_650_10 at center
with dissolve
"지금… 뭐라고 했어?! 누구랑 만난다고?"
"구해준 거에 대한 감사 인사?"
show kaede its_650_01
"웃기지마, 그게 몇 년 전인데! 그걸 왜 이제 와서?"
"그게 아냐, 너한테 흑심이 있는거라고!"
"분명, 분명 나한테서 널 뺏어가려고 할거야!"

menu:
    "1. 그냥 인사일 뿐이야.":
        "넌 몰라. 걘 옛날부터 그랬어… 그냥 호의인 척 하면서 널 노렸다고!"
        show kaede its_650_17
        "정말 모르겠어?"
        "아니면, 그 애가 나보다 좋은거야…?"
        menu:
            "1-1.  억지 부리지 마.":
                show kaede its_650_16
                "억지가 아냐!"
                "왜 그런 소리를 하는거야?"
                "너 설마… 정말로 걔한테 관심 있는거야?"
            "1-2. 그럴리가 없잖아.":
                show kaede its_650_01
                "그럼 만나지 마. 절대 용납 못해."
                "만나기만 해봐... 죽여버릴거야!"



    "2. 나한텐 너밖에 없어, 믿어줘.":
        "그런데 왜 걜 만나려는 거야…?"
        "나보다 걔가 더 중요해?"
        show kaede its_650_07
        "그런거 싫어… "
        menu:
            "2-1. 그렇게 싫으면 가지 않을게.":
                "약속한거지…?"
            "2-2. 넌 날 믿지 않는거야...?":
                "아, 아냐! 널 못 믿는게 아냐."
                "불안해서… 무서워서 그래. 니가 떠나는걸 상상만 해도 버틸수가 없어."
                "날 이해해줘"




$persistent.event650_cleared = True

jump interaction





label event_on_700:
scene black
show kaede mu_whothat at center
with dissolve
"뭐야…? 폰 배경이 왜 여자 사진이야?"
show kaede mu_whothat2
"그렇게 소중한 사람이야?"
show kaede mu_whothat3
"대체 이 여잔 누구야. 누구냐니까!"

menu:
    "그냥 아이돌 사진인데...":
        show kaede mu_whothat4
        "그딴걸 왜 갖고 있는거야?"
        "아니다. 폰 이리내. 내가 직접 지울거야."
        #$persistent.end_killed+=1
    "여동생":
        show kaede mu_yougotsis
        "여동생? 정말?"
        show kaede mu_yougotsis2
        "그럼 나한테 소개시켜줄 수 있겠네?"
        "내일 밤에 너네 집으로 갈게. 괜찮지?"
        menu:
            "물론이지":
                show kaede mu_yougotsis3
                "가서 우리사이를 못받아 둘거야. 그리고 배경은 나로 바꿔 매일 검사할거야."
                "매일 찍어서 보내줄까? 어떤 사진이 좋아?"
                #$persistent.end_lover+=1
            "내일은 곤란해":
                show kaede mu_yougotsis4
                "뭐야… 여동생이라는 거, 거짓말이지?"
                show kaede mu_yougotsis5
                "아니긴 뭘 아냐. 그럼 왜 곤란하다는 건데?"
                show kaede mu_yougotsis6
                "어떤 년인지 몰라도 가만 안 둬"
                #$persistent.end_killed+=1

scene black
show kaede mu_after at center
with fade



$persistent.event700_cleared = True

jump interaction