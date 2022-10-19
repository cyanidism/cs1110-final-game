# Isabella Huang qh8cz
import pygame
import gamebox
import math
# from checkpoint 1
#  my final project is a game that's similar to atari breakout. there's a ball that will freely travel once the player presses a key to start the game. the player has a board that the ball can bounce off of. Then the ball will bounce off obstacles and once it touches an obstacle, the obstacle will be destroyed. the player wins once all the obstacle has been cleared or they will lose if they cannot bounce the ball back in time.
# optional elements: unlike traditional atari breakout with bricks, the obstacles will be monsters so they can be animated.
# there will be a restart option when the player loses to press a key and restart.
# multiple levels: once the player clears all the obstacles in one "room" there will be the option to go to the next level.
# timer: there will be a timer on the harder levels, and the player has to clear all obstacles before the time runs out or else they'll lose.


camera = gamebox.Camera(800, 600)

monster1_frames = gamebox.load_sprite_sheet("Illustration.png", 1, 3)
monster2_frames = gamebox.load_sprite_sheet("Illustration2.png", 1, 3)
monster1 = [gamebox.from_image(80, 50, monster1_frames[1]), gamebox.from_image(240, 50, monster1_frames[1]),
            gamebox.from_image(400, 50, monster1_frames[1]), gamebox.from_image(560, 50, monster1_frames[1]),
            gamebox.from_image(720, 50, monster1_frames[1])]
monster1_level2 = [gamebox.from_image(80, 50, monster1_frames[1]), gamebox.from_image(240, 50, monster1_frames[1]),
                   gamebox.from_image(400, 50, monster1_frames[1]), gamebox.from_image(560, 50, monster1_frames[1]),
                   gamebox.from_image(720, 50, monster1_frames[1])]
monster1_level3 = [gamebox.from_image(80, 50, monster1_frames[1]), gamebox.from_image(240, 50, monster1_frames[1]),
                   gamebox.from_image(400, 50, monster1_frames[1]), gamebox.from_image(560, 50, monster1_frames[1]),
                   gamebox.from_image(720, 50, monster1_frames[1])]
monster2_level2 = [gamebox.from_image(40, 120, monster2_frames[1]), gamebox.from_image(120, 120, monster2_frames[1]),
                   gamebox.from_image(200, 120, monster2_frames[1]), gamebox.from_image(280, 120, monster2_frames[1]),
                   gamebox.from_image(360, 120, monster2_frames[1]), gamebox.from_image(440, 120, monster2_frames[1]),
                   gamebox.from_image(520, 120, monster2_frames[1]), gamebox.from_image(600, 120, monster2_frames[1]),
                   gamebox.from_image(680, 120, monster2_frames[1]), gamebox.from_image(760, 120, monster2_frames[1])]
monster2_level3 = [gamebox.from_image(40, 120, monster2_frames[1]), gamebox.from_image(120, 120, monster2_frames[1]),
                   gamebox.from_image(200, 120, monster2_frames[1]), gamebox.from_image(280, 120, monster2_frames[1]),
                   gamebox.from_image(360, 120, monster2_frames[1]), gamebox.from_image(440, 120, monster2_frames[1]),
                   gamebox.from_image(520, 120, monster2_frames[1]), gamebox.from_image(600, 120, monster2_frames[1]),
                   gamebox.from_image(680, 120, monster2_frames[1]), gamebox.from_image(760, 120, monster2_frames[1])]
platform = gamebox.from_image(400, 600, "platform.png")
platform2 = gamebox.from_image(400, 600, "platform.png")
platform3 = gamebox.from_image(400, 600, "platform.png")
ball = gamebox.from_image(400, 565, "ball.png")
ball2 = gamebox.from_image(400, 565, "ball.png")
ball3 = gamebox.from_image(400, 565, "ball.png")
borders = [gamebox.from_color(400, 0, "lightblue", 800, 0), gamebox.from_color(0, 300, "lightblue", 0, 600),
           gamebox.from_color(800, 300, "lightblue", 0, 600)]
borders2 = [gamebox.from_color(400, 0, "lightblue", 800, 0), gamebox.from_color(0, 300, "lightblue", 0, 600),
            gamebox.from_color(800, 300, "lightblue", 0, 600)]
borders3 = [gamebox.from_color(400, 0, "lightblue", 800, 0), gamebox.from_color(0, 300, "lightblue", 0, 600),
            gamebox.from_color(800, 300, "lightblue", 0, 600)]
ball_speed = 12
ball2_speed = 12
ball3_speed = 12
platform_speed = 15
platform2_speed = 15
platform3_speed = 15
ball.yspeed = 1.3 * ball_speed
ball.xspeed = ball_speed
ball2.yspeed = 1.3 * ball2_speed
ball2.xspeed = ball2_speed
ball3.yspeed = 1.3 * ball3_speed
ball3.xspeed = ball3_speed
current_frame = 0
current_frame2 = 0
current_frame3 = 0
score = 0
score2 = 0
score3 = 0
second = 90
second2 = 90
timer = 2700

game_on = True


def level3_setup(keys):
    global game_on
    global timer
    time = timer//30
    timer -= 1
    time_display = gamebox.from_text(730,570,"Time: "+str(time),40,"red")
    if game_on:
        camera.clear("lightblue")
        camera.draw(platform3)
        camera.draw(ball3)
        camera.draw(time_display)
        # ball speed
        ball3.y -= ball3.yspeed
        ball3.x -= ball3.xspeed

        if pygame.K_LEFT in keys:
            platform3.x -= platform3_speed
        if pygame.K_RIGHT in keys:
            platform3.x += platform3_speed

        # animation
        global current_frame3
        current_frame3 += 0.10
        if current_frame3 > 3:
            current_frame3 = 0

        # collision
        for each in borders3:
            ball.move_to_stop_overlapping(each)
            platform3.move_to_stop_overlapping(each)
            if ball3.touches(each):
                ball3.xspeed = ball3_speed * math.cos(20)
                ball3.yspeed = -1 * ball3_speed
                return ball3.xspeed, ball3.yspeed
        global score3
        for each3 in monster1_level3:
            each3.image = monster1_frames[int(current_frame3)]
            camera.draw(each3)
            ball3.move_to_stop_overlapping(each3)
            if ball3.touches(each3):
                ball3.yspeed = -1.1 * ball3_speed
                ball3.xspeed = -ball3_speed
                each3.x = 9000
                score3 += 1
                return ball3.yspeed, ball3.xspeed
        for each in monster2_level3:
            each.image = monster2_frames[int(current_frame3)]
            camera.draw(each)
            ball3.move_to_stop_overlapping(each)
            if ball3.touches(each):
                ball3.yspeed = -1.1 * ball3_speed
                ball3.xspeed = -ball3_speed
                each.x = 9000
                score3 += 1
                return ball3.yspeed, ball3.xspeed
        ball3.move_to_stop_overlapping(platform3)

        if ball3.touches(platform3):
            ball3.yspeed = -1.1 * ball3.yspeed
            ball3.xspeed = math.cos(30) * ball3_speed
            return ball3.yspeed, ball3.xspeed

        # score_level 3
        score3_display = gamebox.from_text(30, 570, str(score3), 40, "black")
        camera.draw(score3_display)
        # win
        win_sign = gamebox.from_text(400, 300, "YOU WIN!", 72, "black")
        if score3 == 15:
            camera.clear("lightblue")
            ball3.xspeed = 0
            ball3.yspeed = 0
            camera.clear("lightblue")
            camera.draw(win_sign)

        camera.display()
        if ball3.y > 600 or time == 0:
            time = 0
            game_on = False

    if game_on == False:
        # game over
        camera.clear("lightblue")
        game_over = gamebox.from_text(400, 300, "GAME OVER!", 72, "black")
        restart_txt = gamebox.from_text(400, 350, "PRESS SPACE TO RESTART...", 72, "black")
        camera.draw(game_over)
        camera.draw(restart_txt)
        camera.display()

        if pygame.K_SPACE in keys:
            score3 = 0
            timer = 2700
            time = timer // 30
            timer -= 1
            current_frame3 = 0
            current_frame3 += 0.10
            if current_frame3 > 3:
                current_frame3 = 0
            game_on = True
            ball3.x = 500
            ball3.y = 300
            platform3.x = 500
            for each in monster2_level3:
                monster2_level3[0].x = 40
                monster2_level3[1].x = 120
                monster2_level3[2].x = 200
                monster2_level3[3].x = 280
                monster2_level3[4].x = 360
                monster2_level3[5].x = 440
                monster2_level3[6].x = 520
                monster2_level3[7].x = 600
                monster2_level3[8].x = 680
                monster2_level3[9].x = 760
                each.image = monster2_frames[int(current_frame3)]
                camera.draw(each)
            for each in monster1_level3:
                monster1_level3[0].x = 80
                monster1_level3[1].x = 240
                monster1_level3[2].x = 400
                monster1_level3[3].x = 560
                monster1_level3[4].x = 720
                each.image = monster1_frames[int(current_frame3)]
                camera.draw(each)


def level2_setup(keys):
    global game_on
    if game_on:
        camera.clear("lightblue")
        camera.draw(platform2)
        camera.draw(ball2)
        # ball speed
        ball2.y -= ball2.yspeed
        ball2.x -= ball2.xspeed

        if pygame.K_LEFT in keys:
            platform2.x -= platform2_speed
        if pygame.K_RIGHT in keys:
            platform2.x += platform2_speed

        # animation
        global current_frame2
        current_frame2 += 0.10
        if current_frame2 > 3:
            current_frame2 = 0

        # collision
        for each2 in borders2:
            platform2.move_to_stop_overlapping(each2)

            if ball2.touches(each2):
                ball2.yspeed = -1.1 * ball2_speed
                ball2.xspeed = ball2_speed * math.cos(20)
                return ball2.xspeed, ball2.yspeed
        global score2
        for each2 in monster1_level2:
            each2.image = monster1_frames[int(current_frame2)]
            camera.draw(each2)
            ball2.move_to_stop_overlapping(each2)
            if ball2.touches(each2):
                ball2.yspeed = -1.1 * ball2_speed
                ball2.xspeed = -ball2_speed
                each2.x = 9000
                score2 += 1
                return ball2.yspeed, ball2.xspeed
        for each in monster2_level2:
            each.image = monster2_frames[int(current_frame2)]
            camera.draw(each)
            ball2.move_to_stop_overlapping(each)
            if ball2.touches(each):
                ball2.yspeed = -1.1 * ball2_speed
                ball2.xspeed = -ball2_speed
                each.x = 9000
                score2 += 1
                return ball2.yspeed, ball2.xspeed
        ball2.move_to_stop_overlapping(platform2)

        if ball2.touches(platform2):
            ball2.yspeed = -1.1*ball.yspeed
            ball2.xspeed = math.cos(30) * ball2_speed
            return ball2.yspeed, ball2.xspeed

        # score_level 2
        score2_display = gamebox.from_text(30, 570, str(score2), 40, "black")
        camera.draw(score2_display)
        # level 3
        level3 = False
        if score2 == 15:
            camera.clear("lightblue")
            level3 = True
            ball2.x = -1000000
            ball2.y = -10000000000
        global second2
        countdown2 = second2 // 30
        if level3:
            second2 -= 1
            countdown2_display = gamebox.from_text(400, 300, "Level 2: Continue in " + str(countdown2) + "...", 60,
                                                   "black")
            camera.draw(countdown2_display)

        if countdown2 == 0:
            second2 = 0
            return level3_setup(keys)
        camera.display()
        if ball2.bottom > 600:
            game_on = False

    if game_on == False:
        # game over
        camera.clear("lightblue")
        game_over = gamebox.from_text(400, 300, "GAME OVER!", 72, "black")
        restart_txt = gamebox.from_text(400, 350, "PRESS SPACE TO RESTART...", 72, "black")
        camera.draw(game_over)
        camera.draw(restart_txt)
        camera.display()

        if pygame.K_SPACE in keys:
            score2 = 0
            current_frame2 = 0
            current_frame2 += 0.10
            if current_frame2 > 3:
                current_frame2 = 0
            game_on = True
            ball2.x = 500
            ball2.y = 300
            platform2.x = 500
            for each in monster2_level2:
                monster2_level2[0].x = 40
                monster2_level2[1].x = 120
                monster2_level2[2].x = 200
                monster2_level2[3].x = 280
                monster2_level2[4].x = 360
                monster2_level2[5].x = 440
                monster2_level2[6].x = 520
                monster2_level2[7].x = 600
                monster2_level2[8].x = 680
                monster2_level2[9].x = 760
                each.image = monster2_frames[int(current_frame2)]
                camera.draw(each)
            for each in monster1_level2:
                monster1_level2[0].x = 80
                monster1_level2[1].x = 240
                monster1_level2[2].x = 400
                monster1_level2[3].x = 560
                monster1_level2[4].x = 720
                each.image = monster1_frames[int(current_frame2)]
                camera.draw(each)


################################################################################

def tick(keys):
    global game_on

    if game_on == True:
        camera.clear("lightblue")
        camera.draw(platform)
        camera.draw(ball)
        # ball speed
        ball.y -= ball.yspeed
        ball.x -= ball.xspeed

        if pygame.K_LEFT in keys:
            platform.x -= platform_speed
        if pygame.K_RIGHT in keys:
            platform.x += platform_speed

        # animation
        global current_frame
        current_frame += 0.10
        if current_frame > 3:
            current_frame = 0

        # collision
        for each in borders:
            platform.move_to_stop_overlapping(each, 2, 5)
            if ball.touches(each):
                ball.xspeed = ball_speed * math.cos(20)
                ball.yspeed = -1.3 * ball_speed
                return ball.xspeed, ball.yspeed
        global score
        for each in monster1:
            each.image = monster1_frames[int(current_frame)]
            camera.draw(each)
            ball.move_to_stop_overlapping(each)
            if ball.touches(each):
                ball.yspeed = -1.3 * ball_speed
                ball.xspeed = -ball_speed
                each.x = 9000
                score += 1
                return ball.yspeed, ball.xspeed
        ball.move_to_stop_overlapping(platform)

        if ball.touches(platform, 2, 2):
            ball.yspeed = -1.3 * ball.yspeed
            ball.xspeed = math.cos(30) * ball_speed
            return ball.yspeed, ball.xspeed

        # score_level 1
        score_display = gamebox.from_text(30, 570, str(score), 40, "black")
        camera.draw(score_display)

        # level 2
        level2 = False
        if score == 5:
            camera.clear("lightblue")
            level2 = True
            ball.x = -1000000
            ball.y = -10000000000
        global second
        countdown = second // 30
        if level2:
            second -= 1
            countdown_display = gamebox.from_text(400, 300, "Level 2: Continue in " + str(countdown) + "...", 60,
                                                  "black")
            camera.draw(countdown_display)

        if countdown == 0:
            second = 0
            return level2_setup(keys)
        camera.display()
        if ball.bottom > camera.bottom:
            game_on = False

    if game_on == False:
        # game over
        camera.clear("lightblue")
        game_over = gamebox.from_text(400, 300, "GAME OVER!", 72, "black")
        restart_txt = gamebox.from_text(400, 350, "PRESS SPACE TO RESTART...", 72, "black")
        camera.draw(game_over)
        camera.draw(restart_txt)
        camera.display()

        if pygame.K_SPACE in keys:
            score = 0
            current_frame = 0
            current_frame += 0.10
            if current_frame > 3:
                current_frame = 0
            game_on = True
            ball.x = 300
            ball.y = 200
            platform.x = 400
            for each in monster1:
                monster1[0].x = 80
                monster1[1].x = 240
                monster1[2].x = 400
                monster1[3].x = 560
                monster1[4].x = 700
                each.image = monster1_frames[int(current_frame)]
                camera.draw(each)


ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)