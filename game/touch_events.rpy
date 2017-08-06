### touch events on this script


##################################

label touch_g:
python:


    if persistent.love <050:
        jumpPosition = renpy.random.choice(["touch_g_050_01","touch_g_050_02"])
    else:
        if persistent.love<100:

            if persistent.event050_cleared == False:
                jumpPosition = "event_on_050"
            else:
                jumpPosition = renpy.random.choice(["touch_g_100_01"])
        else:
            if persistent.love<200:
                if persistent.event100_cleared == False:
                    jumpPosition = "event_on_100"
                else:
                    jumpPosition = renpy.random.choice(["touch_g_200_01","touch_g_200_02"])
            else:
                if persistent.love<350:

                    if persistent.event200_cleared == False:
                        jumpPosition = "event_on_200"
                    else:
                        jumpPosition = renpy.random.choice(["touch_g_350_01","touch_g_350_02"])
                else:
                    if persistent.love<500:

                        if persistent.event350_cleared == False:
                            jumpPosition = "event_on_350"
                        else:
                            jumpPosition = renpy.random.choice(["touch_g_500_01","touch_g_500_02"])
                    else:
                        if persistent.love<650:

                            if persistent.event500_cleared == False:
                                jumpPosition = "event_on_500"
                            else:
                                jumpPosition = renpy.random.choice(["touch_g_650_01","touch_g_650_02"])
                        else:
                            if persistent.love<700:
                                if persistent.event650_cleared == False:
                                    jumpPosition = "event_on_650"
                                else:
                                    jumpPosition = renpy.random.choice(["touch_g_1000_01","touch_g_1000_02"])
                            else:
                                if persistent.love<1000:
                                    if persistent.event700_cleared == False:
                                        jumpPosition = "event_on_700"
                                    else:
                                        jumpPosition = renpy.random.choice(["touch_g_1000_01","touch_g_1000_02","touch_g_1000_03"])
                                else:
                                    jumpPosition = "endPos"
                           
    persistent.love += 3
jump expression jumpPosition

#################################
label touch_head:
python:
    if persistent.love <050:
        jumpPosition = renpy.random.choice(["touch_head_050_01","touch_head_050_02"])
    else:
        if persistent.love<100:

            if persistent.event050_cleared == False:
                jumpPosition = "event_on_050"
            else:
                jumpPosition = renpy.random.choice(["touch_head_100_01","touch_head_100_02","touch_head_100_03"])
        else:
            if persistent.love<200:
                if persistent.event100_cleared == False:
                    jumpPosition = "event_on_100"
                else:
                    jumpPosition = renpy.random.choice(["touch_head_200_01","touch_head_200_02"])
            else:
                if persistent.love<350:

                    if persistent.event200_cleared == False:
                        jumpPosition = "event_on_200"
                    else:
                        jumpPosition = renpy.random.choice(["touch_head_350_01","touch_head_350_02"])
                else:
                    if persistent.love<500:

                        if persistent.event350_cleared == False:
                            jumpPosition = "event_on_350"
                        else:
                            jumpPosition = renpy.random.choice(["touch_head_500_01","touch_head_500_02"])
                    else:
                        if persistent.love<650:

                            if persistent.event500_cleared == False:
                                jumpPosition = "event_on_500"
                            else:
                                jumpPosition = renpy.random.choice(["touch_head_650_01","touch_head_650_02"])
                        else:
                            if persistent.love<700:
                                if persistent.event650_cleared == False:
                                    jumpPosition = "event_on_650"
                                else:
                                    jumpPosition = renpy.random.choice(["touch_head_1000_01","touch_head_1000_02"])
                            else:
                                if persistent.love<1000:
                                    if persistent.event700_cleared == False:
                                        jumpPosition = "event_on_700"
                                    else:
                                        jumpPosition = renpy.random.choice(["touch_head_1000_01","touch_head_1000_02"])
                                else:
                                    jumpPosition = "endPos"
                           
    persistent.love += 2
jump expression jumpPosition

#################################
label touch_lip:
python:
    if persistent.love <050:
        jumpPosition = renpy.random.choice(["touch_lip_050_01","touch_lip_050_02"])
    else:
        if persistent.love<100:

            if persistent.event050_cleared == False:
                jumpPosition = "event_on_050"
            else:
                jumpPosition = renpy.random.choice(["touch_lip_100_01","touch_lip_100_02"])
        else:
            if persistent.love<200:
                if persistent.event100_cleared == False:
                    jumpPosition = "event_on_100"
                else:
                    jumpPosition = renpy.random.choice(["touch_lip_200_01","touch_lip_200_02"])
            else:
                if persistent.love<350:

                    if persistent.event200_cleared == False:
                        jumpPosition = "event_on_200"
                    else:
                        jumpPosition = renpy.random.choice(["touch_lip_350_01","touch_lip_350_02"])
                else:
                    if persistent.love<500:

                        if persistent.event350_cleared == False:
                            jumpPosition = "event_on_350"
                        else:
                            jumpPosition = renpy.random.choice(["touch_lip_500_01","touch_lip_500_02"])
                    else:
                        if persistent.love<650:

                            if persistent.event500_cleared == False:
                                jumpPosition = "event_on_500"
                            else:
                                jumpPosition = renpy.random.choice(["touch_lip_650_01","touch_lip_650_02"])
                        else:
                            if persistent.love<700:
                                if persistent.event650_cleared == False:
                                    jumpPosition = "event_on_650"
                                else:
                                    jumpPosition = renpy.random.choice(["touch_lip_1000_01","touch_lip_1000_02"])
                            else:
                                if persistent.love<1000:
                                    if persistent.event700_cleared == False:
                                        jumpPosition = "event_on_700"
                                    else:
                                        jumpPosition = renpy.random.choice(["touch_lip_1000_01","touch_lip_1000_02"])
                                else:
                                    jumpPosition = "endPos"
                           
    persistent.love += 3
jump expression jumpPosition

###########################
label touch_boob:
python:
    if persistent.love <050:
        jumpPosition = renpy.random.choice(["touch_boob_050_01","touch_boob_050_02"])
    else:
        if persistent.love<100:

            if persistent.event050_cleared == False:
                jumpPosition = "event_on_050"
            else:
                jumpPosition = renpy.random.choice(["touch_boob_100_01","touch_boob_100_02"])
        else:
            if persistent.love<200:
                if persistent.event100_cleared == False:
                    jumpPosition = "event_on_100"
                else:
                    jumpPosition = renpy.random.choice(["touch_boob_200_01","touch_boob_200_02"])
            else:
                if persistent.love<350:

                    if persistent.event200_cleared == False:
                        jumpPosition = "event_on_200"
                    else:
                        jumpPosition = renpy.random.choice(["touch_boob_350_01","touch_boob_350_02"])
                else:
                    if persistent.love<500:

                        if persistent.event350_cleared == False:
                            jumpPosition = "event_on_350"
                        else:
                            jumpPosition = renpy.random.choice(["touch_boob_500_01","touch_boob_500_02"])
                    else:
                        if persistent.love<650:

                            if persistent.event500_cleared == False:
                                jumpPosition = "event_on_500"
                            else:
                                jumpPosition = renpy.random.choice(["touch_boob_650_01","touch_boob_650_02"])
                        else:
                            if persistent.love<700:
                                if persistent.event650_cleared == False:
                                    jumpPosition = "event_on_650"
                                else:
                                    jumpPosition = renpy.random.choice(["touch_boob_1000_01","touch_boob_1000_02"])
                            else:
                                if persistent.love<1000:
                                    if persistent.event700_cleared == False:
                                        jumpPosition = "event_on_700"
                                    else:
                                        jumpPosition = renpy.random.choice(["touch_boob_1000_01","touch_boob_1000_02"])
                                else:
                                    jumpPosition = "endPos"
                           
    persistent.love += 2
jump expression jumpPosition
####################################


############## 호감도 050 미만일때 ###################


label touch_head_050_01:

show kaede head_touch_suprise

"엣….?"
#$persistent.love+=1
jump interaction

label touch_head_050_02:

show kaede gonlan

"이건 좀 곤란해요"
#$persistent.love+=1
jump interaction

label touch_g_050_01:

show kaede g_touch_hentai

"무슨 짓이에욧!"
#$persistent.love-=1
jump interaction

label touch_g_050_02:

show kaede g_touch_police

"자꾸 이러시면 경찰에 신고 하겠어요."
#$persistent.love-=1
jump interaction

label touch_lip_050_01:

show kaede lip_touch_suprise

"왜 이러세요!"

jump interaction

label touch_lip_050_02:

show kaede lip_touch_moron

"제 입술에 뭐가 묻었나요?"

jump interaction

label touch_boob_050_01:

show kaede boob_touch_pa

"파, 파렴치해요!"
#$persistent.love-=1
jump interaction

label touch_boob_050_02:

show kaede boob_touch_hentai

"그만해 주세요!"
#$persistent.love-=1
jump interaction


label touch_head_100_01:

show kaede me_child

"어린애 취급이냐!"
#$persistent.love+=2
jump interaction


label touch_head_100_02:

show kaede cafe2_wyw

"응? 왜?"
#$persistent.love+=2
jump interaction


label touch_head_100_03:


show kaede cafe2_feel_soso

"...뭐, 나쁘진 않네..."
#$persistent.love+=2

jump interaction



label touch_g_100_01:

show kaede cafe2_feel_dd

"아하하, 간지러워"

jump interaction



label touch_lip_100_01:

show kaede cafe2_lips_on
#$persistent.love+=2
"왜? 뭐 묻었어?"

jump interaction

label touch_lip_100_02:
#$persistent.love+=2
show kaede cafe2_lips_on_shy

"부끄럽게 뭐하는 거야"

jump interaction

label touch_boob_100_01:

show kaede cafe2_scum_boob_on

"뭐, 뭐하는 거야?"
#$persistent.love-=1
jump interaction

label touch_boob_100_02:

show kaede cafe2_scum_boob

"하지말아줘…."
#$persistent.love-=1
jump interaction



############## 호감도 200 미만일때 ###################


label touch_head_200_01:

show kaede th_head_ok

"머리 쓰다듬는거 좋아해?"
#$persistent.love+=2
jump interaction

label touch_head_200_02:

show kaede th_head_hungcle:
"머리 헝크러졌어…"
#$persistent.love+=2

jump interaction

label touch_g_200_01:

show kaede th_u_scum_ide

"......"
#$persistent.love-=1
jump interaction

label touch_g_200_02:

show kaede th_u_scum_ideff

"거긴 왜 자꾸 만지는 거야?"
#$persistent.love-=1
jump interaction

label touch_lip_200_01:

show kaede th_kissshy
#$persistent.love+=2
"왜, 왜…..?"

jump interaction

label touch_lip_200_02:

show kaede th_kissshyheart
#$persistent.love+=2
"...두근거려…"

jump interaction

label touch_boob_200_01:

show kaede th_boob_kack

"꺅!"
#$persistent.love-=1
jump interaction

label touch_boob_200_02:

show kaede th_hentaiu

"변태!"
#$persistent.love-=1
jump interaction




############## 호감도 350 미만일때 ###################


label touch_head_350_01:

show kaede c5_plzmorehead

"좀 더 쓰다듬어줘."
#$persistent.love+=1
jump interaction

label touch_head_350_02:

show kaede c5_plzmorehead2

"기분이 좋아져"
#$persistent.love+=1
jump interaction

label touch_g_350_01:

show kaede c5_bemasexer

"책임지는 거지?"
#$persistent.love+=10
jump interaction

label touch_g_350_02:

show kaede c5_nothear

"여기서 그러면 안돼 ♡"

#$persistent.love+=2
jump interaction

label touch_lip_350_01:
#$persistent.love+=3
show kaede c5_justwannasex

"만지기만 할거야…?"

jump interaction

label touch_lip_350_02:
#$persistent.love+=3
show kaede c5_kissme

"음…"

jump interaction

label touch_boob_350_01:

show kaede c5_wannatouchur

"나도 만져봐도 돼?"
#$persistent.love+=3
jump interaction

label touch_boob_350_02:

show kaede c5_nothear_fornow

"가게에선.. 곤란해"
#$persistent.love+=3
jump interaction



############## 호감도 500 미만일때 ###################


label touch_head_500_01:

show kaede sc_gosex

"계속 머리만 쓰다듬을 거야?"
#$persistent.love+=3
jump interaction

label touch_head_500_02:

show kaede sc_gosex2

"좀 더 아래는 어때?"
#$persistent.love+=3
jump interaction

label touch_g_500_01:

show kaede sc_gosex3

"라면 먹고 갈래?"
#$persistent.love+=8
jump interaction

label touch_g_500_02:

show kaede sc_gosex4

"우리 집 오늘 비는데…"
#$persistent.love+=8
jump interaction

label touch_lip_500_01:

show kaede sc_gosex5

"더 해도 좋은데….."
#$persistent.love+=3
jump interaction

label touch_lip_500_02:

show kaede sc_gosex6

"뭐 묻었어?"
#$persistent.love+=3
jump interaction

label touch_boob_500_01:

show kaede sc_gosex7

"살이 쪘나… 가슴이 좀 커진거 같아. 안그래?"
#$persistent.love+=3
jump interaction

label touch_boob_500_02:

show kaede sc_gosex8

"지금?"
#$persistent.love+=5
jump interaction









############## 호감도 650 미만일때 ###################


label touch_head_650_01:

show kaede th_650_01

"기분 좋아..."
#$persistent.love+=6
jump interaction

label touch_head_650_02:

show kaede th_650_02

"이건 나만의 특권이야. 그치…?"
#$persistent.love+=6
jump interaction





label touch_lip_650_01:

show kaede tl_650_01

"말캉말캉해…"
#$persistent.love+=6
jump interaction

label touch_lip_650_02:

show kaede tl_650_02

"나랑만 하는거지?"
#$persistent.love+=6
jump interaction





label touch_boob_650_01:

show kaede tb_650_01

"거기가 좋아?"
#$persistent.love+=6
jump interaction

label touch_boob_650_02:

show kaede tb_650_02

"네가 원한다면…"
#$persistent.love+=6
jump interaction



label touch_g_650_01:

show kaede tg_650_01

"네가 나만 알았으면 좋겠어."
#$persistent.love+=6
jump interaction

label touch_g_650_02:

show kaede tg_650_02

"기분 좋았어?"
#$persistent.love+=6
jump interaction














############## 호감도 1000 미만일때 ###################


label touch_head_1000_01:

show kaede mu_head

"나한테만 해주는 거지?"
#$persistent.love+=6
jump interaction

label touch_head_1000_02:

show kaede mu_head2

"나 말고는 이러면 절대 안 돼"
#$persistent.love+=6
jump interaction

label touch_g_1000_01:

show kaede mu_gspot

"딴 여자랑도 이러진 않았겠지?"
#$persistent.love+=6
jump interaction


label touch_g_1000_03:

show kaede mu_gspot2

"아랫도리 함부러 놀리면... 잘라버릴거야"
#$persistent.love+=6
jump interaction

label touch_g_1000_02:

show kaede mu_gspot2

"너무 능숙한거 아냐…?"
#$persistent.love+=6
jump interaction

label touch_lip_1000_01:

show kaede mu_kiss1

"딴 사람이랑 하면 죽여버릴거야."
#$persistent.love+=6
jump interaction

label touch_lip_1000_02:

show kaede mu_kiss2

"잘하네…. 어떤 년한테 배운거야?"
#$persistent.love+=6
jump interaction

label touch_boob_1000_01:

show kaede mu_bb1

"나만 만지도록 해"
#$persistent.love+=6
jump interaction

label touch_boob_1000_02:

show kaede mu_bb2

"넌 내꺼지?"
#$persistent.love+=6
jump interaction