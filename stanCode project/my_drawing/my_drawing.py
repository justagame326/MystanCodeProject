"""
File: TOTORO Comes To stanCode SC101 Station
Name: Jerry
----------------------
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GPolygon, GLine, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Title : TOTORO Comes To stanCode SC101 Station

    My childhood favorite cartoon character "TOTORO" comes to "stanCode SC101 Station" to encourage us to take it up
    a notch on coding skill even in raining days.
    """
    window = GWindow(600, 450, title="TOTORO Comes To stanCode SC101 Station")
    background = GRect(600, 450)
    background.filled = True
    background.fill_color = "seagreen"
    window.add(background)

    bottom_body = GOval(240, 350)
    bottom_body.filled = True
    bottom_body.fill_color = "grey"
    window.add(bottom_body, x=317, y=120)

    belly = GOval(204, 170)
    belly.filled = True
    belly.fill_color = "lightgoldenrodyellow"
    window.add(belly, x=335, y=240)

    b1 = GRect(180, 40)
    b1.filled = True
    b1.fill_color = "seagreen"
    b1.color = "seagreen"
    window.add(b1, x=350, y=425)

    l_eye = GOval(25, 25)
    l_eye.filled = True
    l_eye.fill_color = "white"
    window.add(l_eye, x=380, y=170)

    r_eye = GOval(25, 25)
    r_eye.filled = True
    r_eye.fill_color = "white"
    window.add(r_eye, x=460, y=170)

    l_eye_ball = GOval(10, 10)
    l_eye_ball.filled = True
    l_eye_ball.fill_color = "black"
    window.add(l_eye_ball, x=387, y=177)

    r_eye_ball = GOval(10, 10)
    r_eye_ball.filled = True
    r_eye_ball.fill_color = "black"
    window.add(r_eye_ball, x=467, y=177)

    l_eye_ball_white = GOval(4, 4)
    l_eye_ball_white.filled = True
    l_eye_ball_white.fill_color = "white"
    window.add(l_eye_ball_white, x=392, y=182)

    r_eye_ball_white = GOval(4, 4)
    r_eye_ball_white.filled = True
    r_eye_ball_white.fill_color = "white"
    window.add(r_eye_ball_white, x=472, y=182)

    nose = GOval(30, 12)
    nose.filled = True
    nose.fill_color = "black"
    window.add(nose, x=422, y=180)

    mouth = GPolygon()
    mouth.add_vertex((354, 206))
    mouth.add_vertex((514, 206))
    mouth.add_vertex((434, 227))
    mouth.filled = True
    mouth.fill_color = "white"
    window.add(mouth)

    teeth1 = GLine(380, 206, 380, 213)
    window.add(teeth1)

    teeth2 = GLine(406, 206, 406, 220)
    window.add(teeth2)

    teeth3 = GLine(434, 206, 434, 227)
    window.add(teeth3)

    teeth4 = GLine(462, 206, 462, 220)
    window.add(teeth4)

    teeth5 = GLine(488, 206, 488, 213)
    window.add(teeth5)

    l_ear = GPolygon()
    l_ear.add_vertex((390, 135))
    l_ear.add_vertex((400, 130))
    l_ear.add_vertex((398, 125))
    l_ear.add_vertex((402, 120))
    l_ear.add_vertex((392, 75))
    l_ear.add_vertex((390, 75))
    l_ear.add_vertex((380, 127))
    l_ear.add_vertex((382, 127))
    l_ear.add_vertex((390, 125))
    l_ear.filled = True
    l_ear.fill_color = "grey"
    window.add(l_ear)

    r_ear = GPolygon()
    r_ear.add_vertex((470, 127))
    r_ear.add_vertex((480, 132))
    r_ear.add_vertex((483, 125))
    r_ear.add_vertex((490, 126))
    r_ear.add_vertex((484, 75))
    r_ear.add_vertex((482, 75))
    r_ear.add_vertex((465, 117))
    r_ear.add_vertex((475, 120))
    r_ear.add_vertex((473, 125))
    r_ear.filled = True
    r_ear.fill_color = "grey"
    window.add(r_ear)

    l_beard1 = GArc(130, 40, 0, 120)
    window.add(l_beard1, x=270, y=180)

    l_beard2 = GArc(110, 85, 35, 100)
    window.add(l_beard2, x=290, y=189)

    l_beard3 = GArc(130, 80, 65, 100)
    window.add(l_beard3, x=300, y=195)

    r_beard1 = GArc(130, 40, 50, 125)
    window.add(r_beard1, x=495, y=180)

    r_beard2 = GArc(120, 85, 35, 100)
    window.add(r_beard2, x=490, y=188)

    r_beard3 = GArc(110, 40, 0, 120)
    window.add(r_beard3, x=480, y=195)

    body1 = GArc(35, 110, 0, 180)
    body1.filled = True
    body1.fill_color = "darkgrey"
    window.add(body1, x=355, y=280)

    body1_1 = GArc(45, 110, 0, 180)
    body1_1.filled = True
    body1_1.fill_color = "lightgoldenrodyellow"
    body1_1.color = "lightgoldenrodyellow"
    window.add(body1_1, x=352, y=290)

    body2 = GArc(48, 110, 0, 180)
    body2.filled = True
    body2.fill_color = "darkgrey"
    window.add(body2, x=398, y=268)

    body2_1 = GArc(58, 110, 0, 180)
    body2_1.filled = True
    body2_1.fill_color = "lightgoldenrodyellow"
    body2_1.color = "lightgoldenrodyellow"
    window.add(body2_1, x=394, y=278)

    body2a = GArc(38, 100, 0, 180)
    body2a.filled = True
    body2a.fill_color = "darkgrey"
    window.add(body2a, x=453, y=265)

    body2a_1 = GArc(48, 100, 0, 180)
    body2a_1.filled = True
    body2a_1.fill_color = "lightgoldenrodyellow"
    body2a_1.color = "lightgoldenrodyellow"
    window.add(body2a_1, x=449, y=275)

    body3 = GArc(35, 110, 0, 180)
    body3.filled = True
    body3.fill_color = "darkgrey"
    window.add(body3, x=347, y=305)

    body3_1 = GArc(45, 110, 0, 180)
    body3_1.filled = True
    body3_1.fill_color = "lightgoldenrodyellow"
    body3_1.color = "lightgoldenrodyellow"
    window.add(body3_1, x=344, y=315)

    body4 = GArc(42, 105, 0, 180)
    body4.filled = True
    body4.fill_color = "darkgrey"
    window.add(body4, x=387, y=298)

    body4_1 = GArc(52, 105, 0, 180)
    body4_1.filled = True
    body4_1.fill_color = "lightgoldenrodyellow"
    body4_1.color = "lightgoldenrodyellow"
    window.add(body4_1, x=383, y=308)

    body5 = GArc(40, 100, 0, 180)
    body5.filled = True
    body5.fill_color = "darkgrey"
    window.add(body5, x=435, y=294)

    body5_1 = GArc(50, 100, 0, 180)
    body5_1.filled = True
    body5_1.fill_color = "lightgoldenrodyellow"
    body5_1.color = "lightgoldenrodyellow"
    window.add(body5_1, x=431, y=304)

    body6 = GArc(35, 95, 0, 180)
    body6.filled = True
    body6.fill_color = "darkgrey"
    window.add(body6, x=482, y=290)

    body6_1 = GArc(45, 95, 0, 180)
    body6_1.filled = True
    body6_1.fill_color = "lightgoldenrodyellow"
    body6_1.color = "lightgoldenrodyellow"
    window.add(body6_1, x=478, y=300)

    l_hand = GPolygon()
    l_hand.add_vertex((326, 227))
    l_hand.add_vertex((240, 232))
    l_hand.add_vertex((235, 238))
    l_hand.add_vertex((235, 240))
    l_hand.add_vertex((235, 243))
    l_hand.add_vertex((240, 245))
    l_hand.add_vertex((318, 267))
    l_hand.filled = True
    l_hand.fill_color = "grey"
    window.add(l_hand)

    grey_block = GPolygon()
    grey_block.add_vertex((326, 227))
    grey_block.add_vertex((318, 267))
    grey_block.add_vertex((331, 247))
    grey_block.filled = True
    grey_block.fill_color = "grey"
    grey_block.color = "grey"
    window.add(grey_block)

    l_claw1 = GPolygon()
    l_claw1.add_vertex((242, 232))
    l_claw1.add_vertex((239, 234))
    l_claw1.add_vertex((223, 228))
    l_claw1.filled = True
    l_claw1.fill_color = "lightsteelblue"
    window.add(l_claw1)

    l_claw2 = GPolygon()
    l_claw2.add_vertex((237, 235))
    l_claw2.add_vertex((234, 237))
    l_claw2.add_vertex((219, 232))
    l_claw2.filled = True
    l_claw2.fill_color = "lightsteelblue"
    window.add(l_claw2)

    l_claw3 = GPolygon()
    l_claw3.add_vertex((238, 241))
    l_claw3.add_vertex((238, 244))
    l_claw3.add_vertex((219, 236))
    l_claw3.filled = True
    l_claw3.fill_color = "lightsteelblue"
    window.add(l_claw3)

    r_hand = GPolygon()
    r_hand.add_vertex((539, 244))
    r_hand.add_vertex((446, 228))
    r_hand.add_vertex((449, 239))
    r_hand.add_vertex((448, 249))
    r_hand.add_vertex((455, 252))
    r_hand.add_vertex((538, 288))
    r_hand.filled = True
    r_hand.fill_color = "grey"
    window.add(r_hand)

    grey_block1 = GPolygon()
    grey_block1.add_vertex((539, 244))
    grey_block1.add_vertex((538, 288))
    grey_block1.add_vertex((555, 264))
    grey_block1.filled = True
    grey_block1.fill_color = "grey"
    grey_block1.color = "grey"
    window.add(grey_block1)

    u2 = GArc(200, 170, 0, 180)
    u2.filled = True
    u2.fill_color = "lime"
    window.add(u2, x=335, y=30)

    u3 = GArc(100, 170, 0, 180)
    u3.filled = True
    u3.fill_color = "lime"
    window.add(u3, x=385, y=30)

    u4 = GArc(200, 60, 0, 180)
    u4.filled = True
    u4.fill_color = "limegreen"
    window.add(u4, x=335, y=60)

    u5 = GOval(12, 12)
    u5.filled = True
    u5.fill_color = "orange"
    window.add(u5, x=436, y=20)

    u1 = GRect(2, 185)
    u1.filled = True
    u1.fill_color = "lime"
    window.add(u1, x=440, y=60)

    r_claw1 = GPolygon()
    r_claw1.add_vertex((446, 228))
    r_claw1.add_vertex((448, 233))
    r_claw1.add_vertex((428, 228))
    r_claw1.filled = True
    r_claw1.fill_color = "lightsteelblue"
    window.add(r_claw1)

    r_claw2 = GPolygon()
    r_claw2.add_vertex((449, 234))
    r_claw2.add_vertex((448, 238))
    r_claw2.add_vertex((429, 232))
    r_claw2.filled = True
    r_claw2.fill_color = "lightsteelblue"
    window.add(r_claw2)

    r_claw3 = GPolygon()
    r_claw3.add_vertex((450, 240))
    r_claw3.add_vertex((449, 244))
    r_claw3.add_vertex((434, 237))
    r_claw3.filled = True
    r_claw3.fill_color = "lightsteelblue"
    window.add(r_claw3)

    r_claw4 = GPolygon()
    r_claw4.add_vertex((449, 245))
    r_claw4.add_vertex((449, 249))
    r_claw4.add_vertex((432, 242))
    r_claw4.filled = True
    r_claw4.fill_color = "lightsteelblue"
    window.add(r_claw4)

    stop1 = GOval(135, 115)
    stop1.filled = True
    stop1.fill_color = "lemonchiffon"
    window.add(stop1, x=55, y=135)

    stop1 = GOval(125, 105)
    stop1.filled = True
    stop1.fill_color = "lightcyan"
    window.add(stop1, x=60, y=140)

    stop2 = GRect(6, 200)
    stop2.filled = True
    stop2.fill_color = "lavender"
    window.add(stop2, x=120, y=250)

    stop4 = GRect(95, 51)
    stop4.filled = True
    stop4.fill_color = "cornflowerblue"
    window.add(stop4, x=76, y=416)

    stop3 = GArc(160, 80, 220, 100)
    stop3.filled = True
    stop3.fill_color = "lavender"
    window.add(stop3, x=62, y=383)

    label = GLabel("stanCode")
    label.color = "red"
    label.font = "Arial-18-bold"
    window.add(label, x=69, y=187)

    label1 = GLabel("SC101")
    label1.color = "blue"
    label1.font = "Arial-20-bold"
    window.add(label1, x=81, y=215)

    label2 = GLabel("Station")
    label2.color = "green"
    label2.font = "Arial-18-bold"
    window.add(label2, x=82, y=236)

    r1 = GRect(1, 50)
    r1.filled = True
    r1.fill_color = "white"
    r1.color = "white"
    window.add(r1, x=30, y=60)

    r2 = GRect(1, 80)
    r2.filled = True
    r2.fill_color = "white"
    r2.color = "white"
    window.add(r2, x=50, y=115)

    r3 = GRect(1, 40)
    r3.filled = True
    r3.fill_color = "white"
    r3.color = "white"
    window.add(r3, x=80, y=79)

    r4 = GRect(1, 20)
    r4.filled = True
    r4.fill_color = "white"
    r4.color = "white"
    window.add(r4, x=120, y=110)

    r5 = GRect(1, 10)
    r5.filled = True
    r5.fill_color = "white"
    r5.color = "white"
    window.add(r5, x=150, y=30)

    r6 = GRect(1, 80)
    r6.filled = True
    r6.fill_color = "white"
    r6.color = "white"
    window.add(r6, x=150, y=270)

    r7 = GRect(1, 60)
    r7.filled = True
    r7.fill_color = "white"
    r7.color = "white"
    window.add(r7, x=180, y=50)

    r8 = GRect(1, 50)
    r8.filled = True
    r8.fill_color = "white"
    r8.color = "white"
    window.add(r8, x=200, y=60)

    r9 = GRect(1, 80)
    r9.filled = True
    r9.fill_color = "white"
    r9.color = "white"
    window.add(r9, x=220, y=115)

    r10 = GRect(1, 40)
    r10.filled = True
    r10.fill_color = "white"
    r10.color = "white"
    window.add(r10, x=240, y=79)

    r11 = GRect(1, 20)
    r11.filled = True
    r11.fill_color = "white"
    r11.color = "white"
    window.add(r11, x=290, y=110)

    r12 = GRect(1, 10)
    r12.filled = True
    r12.fill_color = "white"
    r12.color = "white"
    window.add(r12, x=320, y=30)

    r13 = GRect(1, 80)
    r13.filled = True
    r13.fill_color = "white"
    r13.color = "white"
    window.add(r13, x=320, y=70)

    r14 = GRect(1, 60)
    r14.filled = True
    r14.fill_color = "white"
    r14.color = "white"
    window.add(r14, x=350, y=50)

    r15 = GRect(1, 50)
    r15.filled = True
    r15.fill_color = "white"
    r15.color = "white"
    window.add(r15, x=130, y=60)

    r16 = GRect(1, 80)
    r16.filled = True
    r16.fill_color = "white"
    r16.color = "white"
    window.add(r16, x=155, y=45)

    r17 = GRect(1, 40)
    r17.filled = True
    r17.fill_color = "white"
    r17.color = "white"
    window.add(r3, x=180, y=79)

    r18 = GRect(1, 20)
    r18.filled = True
    r18.fill_color = "white"
    r18.color = "white"
    window.add(r18, x=220, y=110)

    r19 = GRect(1, 10)
    r19.filled = True
    r19.fill_color = "white"
    r19.color = "white"
    window.add(r19, x=250, y=30)

    r20 = GRect(1, 80)
    r20.filled = True
    r20.fill_color = "white"
    r20.color = "white"
    window.add(r20, x=250, y=70)

    r21 = GRect(1, 60)
    r21.filled = True
    r21.fill_color = "white"
    r21.color = "white"
    window.add(r21, x=480, y=50)

    r23 = GRect(1, 50)
    r23.filled = True
    r23.fill_color = "white"
    r23.color = "white"
    window.add(r23, x=520, y=60)

    r24 = GRect(1, 80)
    r24.filled = True
    r24.fill_color = "white"
    r24.color = "white"
    window.add(r24, x=550, y=115)

    r25 = GRect(1, 40)
    r25.filled = True
    r25.fill_color = "white"
    r25.color = "white"
    window.add(r25, x=560, y=79)

    r26 = GRect(1, 20)
    r26.filled = True
    r26.fill_color = "white"
    r26.color = "white"
    window.add(r26, x=490, y=110)

    r27 = GRect(1, 10)
    r27.filled = True
    r27.fill_color = "white"
    r27.color = "white"
    window.add(r27, x=520, y=30)

    r28 = GRect(1, 80)
    r28.filled = True
    r28.fill_color = "white"
    r28.color = "white"
    window.add(r28, x=520, y=70)

    r29 = GRect(1, 60)
    r29.filled = True
    r29.fill_color = "white"
    r29.color = "white"
    window.add(r29, x=540, y=50)

    r30 = GRect(1, 50)
    r30.filled = True
    r30.fill_color = "white"
    r30.color = "white"
    window.add(r30, x=30, y=350)

    r31 = GRect(1, 80)
    r31.filled = True
    r31.fill_color = "white"
    r31.color = "white"
    window.add(r31, x=55, y=365)

    r32 = GRect(1, 40)
    r32.filled = True
    r32.fill_color = "white"
    r32.color = "white"
    window.add(r32, x=85, y=329)

    r33 = GRect(1, 20)
    r33.filled = True
    r33.fill_color = "white"
    r33.color = "white"
    window.add(r33, x=180, y=310)

    r34 = GRect(1, 10)
    r34.filled = True
    r34.fill_color = "white"
    r34.color = "white"
    window.add(r34, x=180, y=210)

    r35 = GRect(1, 70)
    r35.filled = True
    r35.fill_color = "white"
    r35.color = "white"
    window.add(r35, x=150, y=290)

    r36 = GRect(1, 45)
    r36.filled = True
    r36.fill_color = "white"
    r36.color = "white"
    window.add(r36, x=180, y=310)

    r37 = GRect(1, 50)
    r37.filled = True
    r37.fill_color = "white"
    r37.color = "white"
    window.add(r37, x=270, y=360)

    r38 = GRect(1, 50)
    r38.filled = True
    r38.fill_color = "white"
    r38.color = "white"
    window.add(r38, x=580, y=346)

    r39 = GRect(1, 40)
    r39.filled = True
    r39.fill_color = "white"
    r39.color = "white"
    window.add(r39, x=280, y=380)

    foot = GPolygon()
    foot.add_vertex((432, 415))
    foot.add_vertex((422, 424))
    foot.add_vertex((446, 424))
    foot.filled = True
    foot.fill_color = "black"
    foot.color = "black"
    window.add(foot)

    r_foot1 = GArc(38, 110, 0, 180)
    r_foot1.filled = True
    r_foot1.fill_color = "darkgrey"
    window.add(r_foot1, x=343, y=421)

    r_foot1_1 = GArc(50, 110, 0, 180)
    r_foot1_1.filled = True
    r_foot1_1.fill_color = "seagreen"
    r_foot1_1.color = "seagreen"
    window.add(r_foot1_1, x=338, y=425)

    r_foot2 = GArc(38, 110, 0, 180)
    r_foot2.filled = True
    r_foot2.fill_color = "darkgrey"
    window.add(r_foot2, x=362, y=421)

    r_foot2_1 = GArc(55, 110, 0, 180)
    r_foot2_1.filled = True
    r_foot2_1.fill_color = "seagreen"
    r_foot2_1.color = "seagreen"
    window.add(r_foot2_1, x=358, y=426)

    r_foot3 = GArc(38, 110, 0, 180)
    r_foot3.filled = True
    r_foot3.fill_color = "darkgrey"
    window.add(r_foot3, x=383, y=421)

    r_foot3_1 = GArc(55, 110, 0, 180)
    r_foot3_1.filled = True
    r_foot3_1.fill_color = "seagreen"
    r_foot3_1.color = "seagreen"
    window.add(r_foot3_1, x=377, y=426)

    l_foot3 = GArc(38, 110, 0, 180)
    l_foot3.filled = True
    l_foot3.fill_color = "darkgrey"
    window.add(l_foot3, x=494, y=421)

    l_foot3_1 = GArc(55, 110, 0, 180)
    l_foot3_1.filled = True
    l_foot3_1.fill_color = "seagreen"
    l_foot3_1.color = "seagreen"
    window.add(l_foot3_1, x=482, y=425)

    l_foot2 = GArc(42, 110, 0, 180)
    l_foot2.filled = True
    l_foot2.fill_color = "darkgrey"
    window.add(l_foot2, x=469, y=419)

    l_foot2_1 = GArc(50, 110, 0, 180)
    l_foot2_1.filled = True
    l_foot2_1.fill_color = "seagreen"
    l_foot2_1.color = "seagreen"
    window.add(l_foot2_1, x=464, y=424)

    l_foot1 = GArc(38, 110, 0, 180)
    l_foot1.filled = True
    l_foot1.fill_color = "darkgrey"
    window.add(l_foot1, x=445, y=421)

    l_foot1_1 = GArc(50, 110, 0, 180)
    l_foot1_1.filled = True
    l_foot1_1.fill_color = "seagreen"
    l_foot1_1.color = "seagreen"
    window.add(l_foot1_1, x=437, y=426)

    rect = GRect(30, 55)
    rect.filled = True
    rect.fill_color = "lemonchiffon"
    window.add(rect, x=108, y=270)

    rect1 = GRect(20, 45)
    rect1.filled = True
    rect1.fill_color = "lemonchiffon"
    window.add(rect1, x=113, y=275)

    line1 = GLine(123, 275, 123, 320)
    window.add(line1)

    rect2 = GRect(10, 9)
    rect2.filled = True
    rect2.fill_color = "white"
    window.add(rect2, x=113, y=275)

    rect3 = GRect(10, 9)
    rect3.filled = True
    rect3.fill_color = "white"
    window.add(rect3, x=123, y=284)

    rect4 = GRect(10, 9)
    rect4.filled = True
    rect4.fill_color = "white"
    window.add(rect4, x=113, y=293)

    rect5 = GRect(10, 9)
    rect5.filled = True
    rect5.fill_color = "white"
    window.add(rect5, x=123, y=302)

    rect6 = GRect(10, 9)
    rect6.filled = True
    rect6.fill_color = "white"
    window.add(rect6, x=113, y=311)


if __name__ == '__main__':
    main()
