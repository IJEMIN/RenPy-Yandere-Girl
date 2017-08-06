# 이 파일에는 저작권이 없습니다. 
# 원하는 스크린을 만들 수 있도록 마음껏 수정하세요.

init +1:
    style frame:
        background Frame("ui/inner_frame.png",14,14)

    style button:
        idle_background Frame("ui/inner_frame.png",14,14)
        hover_background Frame("ui/active_frame.png",14,14)
        selected_background Frame("ui/active_frame.png",14,14)
        insensitive_background Frame("ui/inner_frame.png",14,14)
        xminimum 140
        yminimum 60

    style button_text:
        idle_color "#242424"
        selected_color "#FFFFFF"
        insensitive_color "#BDBEC2"
        hover_color "#FFFFFF"
        size 26

    style label_text:
        color "#242424"
        text_align .5

##############################################################################
# 대사 화면
#
# ADV모드 대사를 표시할 때 사용하는 스크린.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:


    # 창을 1개 쓰는 대사창
    window:
        id "window"
        background "#E1E1E1DC"

        has vbox:
            style "say_vbox"

        if who:
            text who id "who"

        text what id "what" xalign 0.5 text_align 0.5 size 42



init -2:
    style say_vbox:
        xfill True
        yalign 0.5
##############################################################################
# 선택지 화면
#
# 게임 내 선택지를 표시할 때 사용하는 스크린.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 24

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear
        size 45

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)



##############################################################################
# 비주얼노벨 대사 화면
#
# NVL모드의 대사와 선택지를 나타낼 때 사용하는 스크린.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # 대사를 표시한다.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # 선택지가 있다면 선택지를 나타낸다.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# 메인 메뉴 화면
#
# 렌파이 게임이 처음 시작되었을 때 나타나는 메인 메뉴를 표시하는 스크린
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:

    # 다른 메뉴 스크린과 교체될 수 있도록 태그를 지정한다.
    tag menu

    # 메인 메뉴 배경 화면.
    window:
        style "mm_root"

    # 메인 메뉴 버튼.
    frame:
        style_group "mm"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Start Game") action Start()
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit(confirm=False)

init -2:

    # 모든 메인 메뉴 버튼이 같은 크기가 되도록 한다.
    style mm_button:
        size_group "mm"



##############################################################################
# 네비게이션 화면
#
# 게임 메뉴 네비게이션 버튼과 배경 화면을 표시하는 스크린이 포함된 스크린.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # 게임 메뉴 배경 화면.
    window:
        style "gm_root"

    # 여러 가지 버튼.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:

    # 모든 네비게이션 버튼이 같은 크기가 되도록 한다.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# 저장하기, 불러오기 화면
#
# 게임을 저장하거나 불러올 수 있는 화면.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# 저장하기와 불러오기는 기능이 비슷하기 때문에, file_picker라는 스크린 하나에 통합했습니다.
# 그리고 file_picker 스크린을 load 및 save 스크린에 간단히 추가했습니다.

screen save:
    tag menu
    timer 0.1 action Return()

screen load:
    tag menu
    timer 0.1 action Return()

    # 다른 메뉴 스크린으로 교체할 수 있도록 태그를 추가한다.
##############################################################################
# 환경설정 화면
#
# 환경설정을 변경할 수 있는 스크린.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences:
    

    tag menu

    # 환경설정 메뉴들을 3x1 행렬로 배치한다.
    button:
        xfill True
        yfill True
        xmargin 0
        ymargin 0
        background "#262626DC"
        action Return()

    frame:
        xpadding 10
        ypadding 10
        xalign .5
        yalign .5
        vbox:
            spacing 18
            xalign .5

            frame:
                vbox:
                    spacing 10
                    label "I_Jemin 제작" text_size 50 xalign .5
                    null height 10
                    label "*Contact*\ni_jemin@hotmail.com\n@i_jemin" text_size 30 xalign .5 text_style "contactInfo_text"
            textbutton "보이스 OFF" action Preference("voice mute", "toggle") xalign .5
            textbutton "배경음 OFF" action Preference("music mute", "toggle") xalign .5
            textbutton "엔딩 리스트" action ShowMenu("ending_list") xalign .5
            if persistent.game_cleared == True:
                textbutton "외형 변경" action ShowMenu("fit_list") xalign .5
            else:
                textbutton "외형 변경" xalign .5


init -2:
    style contactInfo_text:
        line_spacing 8
        text_align .5

    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0


##############################################################################
# 예/아니오 확인 화면
#
# 예 또는 아니오를 묻는 스크린.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt


screen ending_list:
    
    button:
        background "#262626DC"
        xfill True
        yfill True
        xmargin 0
        ymargin 0
        action Return()

        frame:
            background Frame("ui/container_frame.png",14,14)
            xalign 0.5
            yalign 0.5
            xpadding 20
            ypadding 50

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 20

                frame:
                    xsize 400
                    if persistent.ending_1_cleared == True :
                        label "엔딩 1-1\n그대의 눈동자에 건배(찡긋)" text_size 40 xalign .5
                    else :
                        label "엔딩 1-1\n????" text_size 40 xalign .5


                frame:
                    xsize 400
                    if persistent.ending_2_cleared == True :
                        label "엔딩 1-2\n널 가질수 없다면 박제해버리겠어"  text_size 40 xalign .5
                    else :
                        label "엔딩 1-2\n????" text_size 40 xalign .5


                frame:
                    xsize 400
                    if persistent.ending_3_cleared == True :
                        label "엔딩 1-3\n전기톱은 훌륭한 대화수단" text_size 40 xalign .5
                    else :
                        label "엔딩 1-3\n????" text_size 40 xalign .5


                frame:
                    xsize 400
                    if persistent.ending_4_cleared == True :
                        label "엔딩 2-1\n눈새" text_size 40 xalign .5
                    else:
                        label "엔딩 2-1\n????" text_size 40 xalign .5


                frame:
                    xsize 400
                    if persistent.ending_5_cleared == True :
                        label "엔딩 2-2\n난 (척추)신경이 없어" text_size 40 xalign .5
                    else:
                        label "엔딩 2-2\n????" text_size 40 xalign .5


                frame:
                    xsize 400
                    if persistent.ending_6_cleared == True:
                        label "엔딩 3-1\n못지킬 약속" text_size 40 xalign .5
                    else:
                        label "엔딩 3-1\n????" text_size 40 xalign .5

                frame:
                    xsize 400
                    if persistent.ending_7_cleared == True:
                        label "엔딩 3-2\n의사부부" text_size 40 xalign .5
                    else:
                        label "엔딩 3-2\n????" text_size 40 xalign .5


                frame:
                    xsize 400
                    if persistent.ending_8_cleared == True:
                        label "엔딩 3-3\n참교육자 - 아랫도리 돈 두댓" text_size 40 xalign .5
                    else:
                        label "엔딩 3-3\n????" text_size 40 xalign .5



screen yesno_prompt:

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

    # 마우스 우클릭과 esc 키는 No 버튼과 같다.
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# 단축 메누 화면
#
# say 스크린에 기본적으로 포함되어 일부 유용한 기능을
# 빠르게 사용할 수 있는 버튼이 포함된 스크린.


init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"


    transform invisible:
        alpha 0
   
screen interaction_screen:
    use touch_spot
    use conversation_button
    timer 10 action Jump("waiting")
    vbox:
        spacing 15
        xalign 0.98 yalign 0.01

        textbutton "환경설정" action ShowMenu("preferences") 

       # textbutton "나가기" action Jump("quiting") xalign 0.98 yalign 0.01
        textbutton "나가기" action Jump("quiting")


        

screen conversation_button:
    textbutton "대화하기" action Jump("conversation"):
        xpadding 20
        ypadding 20
        text_size 80
        xalign 0.5
        
    
        yalign 0.8

screen end_button:
    textbutton "대화하기" action Return():
        text_size 80
        xalign 0.5
        
        
        yalign 0.8


screen touch_spot:
    
    textbutton "머리 터치 지점" action Jump("touch_head") at invisible:
        xalign 0.46 yalign 0.07 xsize 279 ysize 130

    textbutton "입술 터치 지점" action Jump("touch_lip") at invisible:
        xalign 0.467 yalign 0.25


    textbutton "가슴 터치 지점" action Jump("touch_boob") at invisible:
        xalign 0.46 yalign 0.4 xsize 279 ysize 140

    textbutton "하체 터치 지점" action Jump("touch_g") at invisible:
        xalign 0.465 yalign 0.65 xsize 293 ysize 140

screen love_point:
    $ display_text = "호감도 " + str(persistent.love)
    
    frame:
        xalign 0.04 yalign 0.01
        label display_text:
            
            text_size 50

screen fit_list:

    tag menu
    button:
        background "#262626DC"
        xfill True
        yfill True
        xmargin 0
        ymargin 0
        action Return()

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 10
        ypadding 10
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5
            textbutton "하양" text_size 50 action Jump("to_white")
            textbutton "분홍" text_size 50 action Jump("to_pink")
            textbutton "금발" text_size 50 action Jump("to_blond")
            textbutton "초록" text_size 50 action Jump("to_green")
            textbutton "흑발" text_size 50 action Jump("to_black")
