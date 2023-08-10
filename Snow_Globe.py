from Focus_Roots import *


cloud_middle1=105
cloud_right1=160
cloud_left1=50

cloud_middle2 = 400
cloud_right2 = 450
cloud_left2 = 340

cloud_middle3 = 250
cloud_right3 = 305
cloud_left3 = 195

cloud_middle4 = 250
cloud_right4 = 305
cloud_left4 = 195

snowball = 150
snowball_pos2 = 200
snowball_pos3 = 225
snowball_pos4 = 175

character_pos = 150

def change():
    global cloud_middle1,cloud_right1,cloud_left1,cloud_left2,cloud_middle2, cloud_right2
    global cloud_middle3, cloud_right3, cloud_left3, cloud_middle4, cloud_right4, cloud_left4, snowball, snowball_pos2, snowball_pos3, snowball_pos4
    global character_pos

    set_background(color_blue)#This will set the background
    draw_rect(0, 350, 500, 250, 0, color_white)#ground
    
    draw_rect(character_pos, 325, 25, 25, 0)#player

    #Snowballs on the left

    draw_circle(260, snowball, 5, 0, color_white)
    draw_circle(280, snowball_pos2, 5, 0, color_white)
    draw_circle(300, snowball, 5, 0, color_white)
    draw_circle(320, snowball_pos2, 5, 0, color_white)
    draw_circle(340, snowball, 5, 0, color_white)
    draw_circle(360, snowball_pos2, 5, 0, color_white)
    draw_circle(380, snowball, 5, 0, color_white)
    draw_circle(400, snowball_pos2, 5, 0, color_white)
    draw_circle(420, snowball, 5, 0, color_white)
    draw_circle(440, snowball_pos2, 5, 0, color_white)
    draw_circle(460, snowball, 5, 0, color_white)
    draw_circle(480, snowball_pos2, 5, 0, color_white)
    draw_circle(500, snowball, 5, 0, color_white)

    draw_circle(260, snowball_pos3, 5, 0, color_white)
    draw_circle(280, snowball_pos4, 5, 0, color_white)
    draw_circle(300, snowball_pos3, 5, 0, color_white)
    draw_circle(320, snowball_pos4, 5, 0, color_white)
    draw_circle(340, snowball_pos3, 5, 0, color_white)
    draw_circle(360, snowball_pos4, 5, 0, color_white)
    draw_circle(380, snowball_pos3, 5, 0, color_white)
    draw_circle(400, snowball_pos4, 5, 0, color_white)
    draw_circle(420, snowball_pos3, 5, 0, color_white)
    draw_circle(440, snowball_pos4, 5, 0, color_white)
    draw_circle(460, snowball_pos3, 5, 0, color_white)
    draw_circle(480, snowball_pos4, 5, 0, color_white)
    draw_circle(500, snowball_pos3, 5, 0, color_white)
    
    #Snowballs on the right
    draw_circle(0, snowball, 5, 0, color_white)
    draw_circle(20, snowball_pos2, 5, 0, color_white)
    draw_circle(40, snowball, 5, 0, color_white)
    draw_circle(60, snowball_pos2, 5, 0, color_white)
    draw_circle(80, snowball, 5, 0, color_white)
    draw_circle(100, snowball_pos2, 5, 0, color_white)
    draw_circle(120, snowball, 5, 0, color_white)
    draw_circle(140, snowball_pos2, 5, 0, color_white)
    draw_circle(160, snowball, 5, 0, color_white)
    draw_circle(180, snowball_pos2, 5, 0, color_white)
    draw_circle(200, snowball, 5, 0, color_white)
    draw_circle(220, snowball_pos2, 5, 0, color_white)
    draw_circle(240, snowball, 5, 0, color_white)

    draw_circle(0, snowball_pos3, 5, 0, color_white)
    draw_circle(20, snowball_pos4, 5, 0, color_white)
    draw_circle(40, snowball_pos3, 5, 0, color_white)
    draw_circle(60, snowball_pos4, 5, 0, color_white)
    draw_circle(80, snowball_pos3, 5, 0, color_white)
    draw_circle(100, snowball_pos4, 5, 0, color_white)
    draw_circle(120, snowball_pos3, 5, 0, color_white)
    draw_circle(140, snowball_pos4, 5, 0, color_white)
    draw_circle(160, snowball_pos3, 5, 0, color_white)
    draw_circle(180, snowball_pos4, 5, 0, color_white)
    draw_circle(200, snowball_pos3, 5, 0, color_white)
    draw_circle(220, snowball_pos4, 5, 0, color_white)
    draw_circle(240, snowball_pos3, 5, 0, color_white)

    #Clouds
    draw_circle(cloud_middle1, 150, 70, 0, color = color_gray)
    draw_circle(cloud_right1, 150, 50, 0, color = color_gray)#cloud 1
    draw_circle(cloud_left1, 150, 50, 0, color = color_gray)

    draw_circle(cloud_middle2, 150, 70, 0, color = color_gray)
    draw_circle(cloud_right2, 150, 50, 0, color = color_gray)#cloud 2
    draw_circle(cloud_left2, 150, 50, 0, color = color_gray)

    draw_circle(cloud_middle3, 150, 70, 0, color = color_gray)
    draw_circle(cloud_right3, 150, 50, 0, color = color_gray)#cloud 3
    draw_circle(cloud_left3, 150, 50, 0, color = color_gray)

    draw_circle(cloud_middle4, 150, 70, 0, color = color_gray)
    draw_circle(cloud_right4, 150, 50, 0, color = color_gray)#cloud 4
    draw_circle(cloud_left4, 150, 50, 0, color = color_gray)

    #Extra Clouds
    draw_circle(500, 150, 70, 0, color_gray)
    draw_circle(0, 150, 70, 0, color_gray)
    draw_circle(450, 150, 50, 0, color_gray)
    draw_circle(50, 150, 50, 0, color_gray)

    #Animations
    cloud_middle1=cloud_middle1+0.20
    cloud_right1=cloud_right1+0.20 # Cloud 1 Animation
    cloud_left1=cloud_left1+0.20

    cloud_middle2=cloud_middle2-0.20
    cloud_right2=cloud_right2-0.20 # Cloud 2 Animation
    cloud_left2=cloud_left2-0.20

    cloud_middle3 = cloud_middle3-0.20
    cloud_right3 = cloud_right3-0.20 # cloud 3 Animation
    cloud_left3 = cloud_left3-0.20

    cloud_middle4 = cloud_middle4+0.20
    cloud_right4 = cloud_right4+0.20 # cloud 4 Animation
    cloud_left4 = cloud_left4+0.20


    snowball = snowball+0.5
    snowball_pos2 = snowball_pos2+0.5
    snowball_pos3 = snowball_pos3+0.5
    snowball_pos4 = snowball_pos4+0.5

    character_pos = character_pos+0.5



draw(change)