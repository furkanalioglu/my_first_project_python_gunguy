
from graphics import Canvas
import time
import random

NEW_HITBOX_CHANCE = 0.02

def gun_guy(canvas):
    gun_man = canvas.create_rectangle(0,0,50,50)
    canvas.moveto(gun_man,400,500)
    canvas.update()
    
def add_score_label(canvas, score):

    label = canvas.create_text(65, canvas.get_canvas_height()- 10, "")
    canvas.set_font(label, "Courier", 20)
    update_score_label(canvas, label, score)
    return label


def update_score_label(canvas, score_label, score):
    canvas.set_text(score_label, "Score: " + str(score))
    


def starting_screen(canvas,score):
    IDUVIA = canvas.create_text(canvas.get_canvas_width()//2, (canvas.get_canvas_height()//2)-100, 'WELCOME TO GUNGUY')
    start_button = canvas.create_rectangle(250, 300, 550, 400)
    start_text = canvas.create_text(400, 350, 'START')
    canvas.set_font(start_text,'Times',50)
    canvas.set_font(IDUVIA, 'Times', 25)
    canvas.set_fill_color(start_button, 'red')
    
    while True:
        clicks = canvas.get_new_mouse_clicks()
        for click in clicks:
            clicked_object = canvas.find_element_at(click.x, click.y)
            if clicked_object and clicked_object == start_button:
                canvas.delete(start_button)
                canvas.delete(start_text)
                canvas.delete(IDUVIA)
                level1(canvas,score)
                break
            elif clicked_object and clicked_object == start_text:
                canvas.delete(start_button)
                canvas.delete(start_text)
                canvas.delete(IDUVIA)
                level1(canvas,score)
                break
            canvas.update()
        canvas.update()
        
        
def GAMEOVERSCREEN(canvas,score):
    IDUVIA = canvas.create_text(canvas.get_canvas_width()//2, (canvas.get_canvas_height()//2)-100, 'YOU LOSE')
    start_button = canvas.create_rectangle(250, 300, 550, 400)
    start_text = canvas.create_text(400, 350, 'CLICK TO START AGAIN')
    score_count = canvas.create_text((canvas.get_canvas_width()//2) + 75, 550, score)
    score_txxt = canvas.create_text(canvas.get_canvas_width()//2, 550, 'SCORE: ')
    canvas.set_font(start_text,'Times',15)
    canvas.set_font(IDUVIA, 'Times', 25)
    canvas.set_font(score_count, 'Times', 25)
    canvas.set_font(score_txxt, 'Times', 25)
    canvas.set_fill_color(start_button, 'yellow')
    score = 0
    
    while True:
        clicks = canvas.get_new_mouse_clicks()
        for click in clicks:
            clicked_object = canvas.find_element_at(click.x, click.y)
            if clicked_object and clicked_object == start_button:
                canvas.delete(start_button)
                canvas.delete(start_text)
                canvas.delete(IDUVIA)
                level1(canvas,score)
                break
            elif clicked_object and clicked_object == start_text:
                canvas.delete(start_button)
                canvas.delete(start_text)
                canvas.delete(IDUVIA)
                level1(canvas,score)
                break
            canvas.update()
        canvas.update()
    
# -----------------------------------------


def main_ground(canvas):
    flat = canvas.create_rectangle(-10,500,800,600)
    canvas.set_fill_color(flat, 'snow')


def clouds(canvas):
    SIZE_X = 200
    SIZE_Y = 20
    x_circle = 50
    y_circle = 25
    for i in range(3):
        bulut1 = canvas.create_oval(x_circle,y_circle,x_circle+SIZE_X,y_circle+SIZE_Y)
        canvas.set_fill_color(bulut1, 'antique white')
        x_circle +=250
        

        
def level1(canvas,score):
    canvas.delete_all()
    main_ground(canvas)
    clouds(canvas)
    score_label = add_score_label(canvas, score)
    canvas.update()
    gun_man = canvas.create_rectangle(0,0,50,100)
    canvas.set_fill_color(gun_man, 'red')
    canvas.moveto(gun_man,0,400)
    main_bullet = canvas.create_oval(50,canvas.get_mouse_y(),75,canvas.get_mouse_y()+25)
    canvas.set_fill_color(main_bullet,canvas.get_random_color())
    canvas.move(main_bullet, 0,200)
    # ----------------------------------------------------------------------- LEVEL 1
    RANDOM_SIZE = random.randint(30, 50)
    RANDOM_Y = random.randint(100, 255)
    green_hitboxx = canvas.create_oval(750,RANDOM_Y,800,RANDOM_Y+RANDOM_SIZE)
    RANDOM_SIZE = random.randint(30, 120)
    RANDOM_Y = random.randint(256, 450)
    red_hitboxx = canvas.create_oval(750,RANDOM_Y,800,RANDOM_Y+RANDOM_SIZE)
    canvas.set_fill_color(red_hitboxx, 'red')
    canvas.set_fill_color(green_hitboxx, 'green')
    # --------------------------------------------------------------------
    
    while True:
        mouse_y = canvas.get_mouse_y()
        clicks = canvas.get_new_mouse_clicks()
        if mouse_y > 75 and mouse_y < 400:
            canvas.moveto(gun_man, 0,mouse_y)
        if mouse_y > 75 and mouse_y < 400 and canvas.get_left_x(main_bullet) < 80:
            canvas.moveto(main_bullet, 50, mouse_y+35)
        if canvas.get_left_x(main_bullet) > 60 and canvas.get_left_x(main_bullet) < 800:
            canvas.move(main_bullet, 20, 0)
        elif canvas.get_left_x(main_bullet) >= 800:
            canvas.moveto(main_bullet, 50, mouse_y+35)
        if clicks and canvas.get_left_x(main_bullet) < 60:
            canvas.move(main_bullet, 30, 0)
        collided_object = canvas.find_element_at(canvas.get_left_x(main_bullet), canvas.get_top_y(main_bullet))
        if collided_object and collided_object == green_hitboxx:
            canvas.delete(green_hitboxx)
            score += 1
            level2(canvas,score)
            break
        if collided_object and collided_object == red_hitboxx:
            canvas.move(green_hitboxx,-45,0)
        if canvas.get_left_x(green_hitboxx) <= 75 or canvas.get_left_x(red_hitboxx) <= 0:
            canvas.delete_all()
            GAMEOVERSCREEN(canvas,score)
            break
        ghw1 = -0.5
        ghw2 = -0.5
        hiz = random.randint(-7,-3)
        canvas.move(green_hitboxx, hiz, ghw1)
        hiz = random.randint(-7,-3)
        canvas.move(red_hitboxx,hiz,ghw2)
        if canvas.get_top_y(green_hitboxx) + 60 > 400 or canvas.get_top_y(green_hitboxx) <100:
            ghw1 = - ghw1
        if canvas.get_top_y(red_hitboxx) + 60 >=400 or canvas.get_top_y(red_hitboxx) <100:
            ghw2 = - ghw2
            
        canvas.update()
        time.sleep(0.02)

def level2(canvas,score):
    canvas.delete_all()
    main_ground(canvas)
    clouds(canvas)
    score_label = add_score_label(canvas, score)
    canvas.update()
    gun_man = canvas.create_rectangle(0,0,50,100)
    canvas.set_fill_color(gun_man, 'red')
    canvas.moveto(gun_man,0,400)
    main_bullet = canvas.create_oval(50,canvas.get_mouse_y(),75,canvas.get_mouse_y()+25)
    canvas.set_fill_color(main_bullet,canvas.get_random_color())
    canvas.move(main_bullet, 0,200)
    # ----------------------------------------------------------------------- LEVEL 1
    RANDOM_SIZE = random.randint(30, 50)
    RANDOM_Y = random.randint(256, 450)
    red_hitboxx = canvas.create_oval(750,RANDOM_Y,800,RANDOM_Y+RANDOM_SIZE)
    RANDOM_SIZE = random.randint(30, 75)
    RANDOM_Y = random.randint(100, 180)
    green_hitboxx = canvas.create_oval(750,RANDOM_Y,800,RANDOM_Y+RANDOM_SIZE)
    canvas.set_fill_color(red_hitboxx, 'red')
    canvas.set_fill_color(green_hitboxx, 'green')
    RANDOM_SIZE = random.randint(30, 40)
    RANDOM_Y = random.randint(200, 255)
    yellow_hitboxx = canvas.create_oval(750,RANDOM_Y,800,RANDOM_Y+RANDOM_SIZE)
    canvas.set_fill_color(yellow_hitboxx, 'yellow')
    
    # --------------------------------------------------------------------
    while True:
        mouse_y = canvas.get_mouse_y()
        clicks = canvas.get_new_mouse_clicks()
        if mouse_y > 75 and mouse_y < 400:
            canvas.moveto(gun_man, 0,mouse_y)
        if mouse_y > 75 and mouse_y < 400 and canvas.get_left_x(main_bullet) < 80:
            canvas.moveto(main_bullet, 50, mouse_y+35)
        if canvas.get_left_x(main_bullet) > 60 and canvas.get_left_x(main_bullet) < 800:
            canvas.move(main_bullet, 20, 0)
        elif canvas.get_left_x(main_bullet) >= 800:
            canvas.moveto(main_bullet, 50, mouse_y+35)
        if clicks and canvas.get_left_x(main_bullet) < 60:
            canvas.move(main_bullet, 30, 0)
        collided_object = canvas.find_element_at(canvas.get_left_x(main_bullet), canvas.get_top_y(main_bullet))
        if collided_object and collided_object == green_hitboxx:
            canvas.delete(green_hitboxx)
            score += 1
            level3(canvas,score)
            break
        if collided_object and collided_object == red_hitboxx:
            canvas.move(green_hitboxx,-45,0)
        if collided_object and collided_object == yellow_hitboxx:
            canvas.move(green_hitboxx,0,100)
        if canvas.get_left_x(green_hitboxx) <= 75 or canvas.get_left_x(red_hitboxx) <= 0:
            canvas.delete_all()
            GAMEOVERSCREEN(canvas,score)
            break

        ghw1 = -1
        ghw2 = -1 
        hiz = random.randint(-15,-7)
        canvas.move(green_hitboxx, hiz, ghw1)
        hiz = random.randint(-15,-7)
        canvas.move(red_hitboxx,hiz,ghw2)
        canvas.move(yellow_hitboxx,hiz,ghw1)
        if canvas.get_top_y(green_hitboxx) + 60 >=400 or canvas.get_top_y(green_hitboxx) <100:
            ghw1 = - ghw1
        if canvas.get_top_y(red_hitboxx) + 60 >=400 or canvas.get_top_y(red_hitboxx) <100:
            ghw2 = - ghw2
        if canvas.get_top_y(yellow_hitboxx) + 60 >=400 or canvas.get_top_y(yellow_hitboxx) <100:
            ghw2 = - ghw2
        canvas.update()
        time.sleep(0.02)
        
        
        
def level3(canvas,score):
    canvas.delete_all()
    main_ground(canvas)
    clouds(canvas)
    score_label = add_score_label(canvas, score)
    canvas.update()
    gun_man = canvas.create_rectangle(0,0,50,100)
    canvas.set_fill_color(gun_man, 'red')
    canvas.moveto(gun_man,0,400)
    main_bullet = canvas.create_oval(50,canvas.get_mouse_y(),75,canvas.get_mouse_y()+25)
    canvas.set_fill_color(main_bullet,canvas.get_random_color())
    canvas.move(main_bullet, 0,200)
    # ----------------------------------------------------------------------- LEVEL 1
    RANDOM_SIZE = random.randint(30, 50)
    RANDOM_Y = random.randint(256, 450)
    green_hitboxx = canvas.create_oval(750,RANDOM_Y,800,RANDOM_Y+RANDOM_SIZE)
    RANDOM_SIZE = random.randint(30, 120)
    RANDOM_Y = random.randint(100, 255)
    red_hitboxx = canvas.create_oval(750,RANDOM_Y,800,RANDOM_Y+RANDOM_SIZE)
    canvas.set_fill_color(red_hitboxx, 'red')
    canvas.set_fill_color(green_hitboxx, 'green')
    # --------------------------------------------------------------------
    while True:
        mouse_y = canvas.get_mouse_y()
        clicks = canvas.get_new_mouse_clicks()
        if mouse_y > 75 and mouse_y < 400:
            canvas.moveto(gun_man, 0,mouse_y)
        if mouse_y > 75 and mouse_y < 400 and canvas.get_left_x(main_bullet) < 80:
            canvas.moveto(main_bullet, 50, mouse_y+35)
        if canvas.get_left_x(main_bullet) > 60 and canvas.get_left_x(main_bullet) < 800:
            canvas.move(main_bullet, 20, 0)
        elif canvas.get_left_x(main_bullet) >= 800:
            canvas.moveto(main_bullet, 50, mouse_y+35)
        if clicks and canvas.get_left_x(main_bullet) < 60:
            canvas.move(main_bullet, 30, 0)
        collided_object = canvas.find_element_at(canvas.get_left_x(main_bullet), canvas.get_top_y(main_bullet))
        if collided_object and collided_object == green_hitboxx:
            canvas.delete(green_hitboxx)
            score += 1
            level4(canvas,score)
            break
        if collided_object and collided_object == red_hitboxx:
            canvas.move(green_hitboxx,-45,0)
        if canvas.get_left_x(green_hitboxx) <= 75 or canvas.get_left_x(red_hitboxx) <= 0:
            canvas.delete_all()
            GAMEOVERSCREEN(canvas,score)
            break
            
        hiz = random.randint(-20,-10)
        ghw1 = -1.5
        ghw2 = -1.5
        canvas.move(green_hitboxx, hiz, ghw1)
        hiz = random.randint(-15,-7)
        canvas.move(red_hitboxx,hiz,ghw2)
        if canvas.get_top_y(green_hitboxx) + 60 >=400 or canvas.get_top_y(green_hitboxx) <100:
            ghw1 = - ghw1
        if canvas.get_top_y(red_hitboxx) + 60 >=500 or canvas.get_top_y(red_hitboxx) <100:
            ghw2 = - ghw2
        canvas.update()
        time.sleep(0.02)
        
        
        
def level4(canvas,score):
    canvas.delete_all()
    main_ground(canvas)
    clouds(canvas)
    score_label = add_score_label(canvas, score)
    canvas.update()
    gun_man = canvas.create_rectangle(0,0,50,100)
    canvas.set_fill_color(gun_man, 'red')
    canvas.moveto(gun_man,0,400)
    main_bullet = canvas.create_oval(50,canvas.get_mouse_y(),75,canvas.get_mouse_y()+25)
    canvas.set_fill_color(main_bullet,canvas.get_random_color())
    canvas.move(main_bullet, 0,200)
    # ----------------------------------------------------------------------- LEVEL 1
    RANDOM_SIZE = random.randint(30, 75)
    RANDOM_Y = random.randint(400,450)
    green_hitboxx = canvas.create_oval(750,RANDOM_Y,800,RANDOM_Y+RANDOM_SIZE)
    RANDOM_SIZE = random.randint(30, 50)
    RANDOM_Y = random.randint(150, 250)
    red_hitboxx = canvas.create_oval(750,RANDOM_Y,800,RANDOM_Y+RANDOM_SIZE)
    canvas.set_fill_color(red_hitboxx, 'red')
    canvas.set_fill_color(green_hitboxx, 'green')
    RANDOM_SIZE = random.randint(30, 80)
    RANDOM_Y = random.randint(170, 430)
    blau_hitboxx = canvas.create_oval(750,RANDOM_Y,800,RANDOM_Y+RANDOM_SIZE)
    canvas.set_fill_color(blau_hitboxx,'blue')
    # --------------------------------------------------------------------
    
    while True:
        mouse_y = canvas.get_mouse_y()
        clicks = canvas.get_new_mouse_clicks()
        if mouse_y > 75 and mouse_y < 400:
            canvas.moveto(gun_man, 0,mouse_y)
        if mouse_y > 75 and mouse_y < 400 and canvas.get_left_x(main_bullet) < 80:
            canvas.moveto(main_bullet, 50, mouse_y+35)
        if canvas.get_left_x(main_bullet) > 60 and canvas.get_left_x(main_bullet) < 800:
            canvas.move(main_bullet, 20, 0)
        elif canvas.get_left_x(main_bullet) >= 800:
            canvas.moveto(main_bullet, 50, mouse_y+35)
        if clicks and canvas.get_left_x(main_bullet) < 60:
            canvas.move(main_bullet, 30, 0)
        collided_object = canvas.find_element_at(canvas.get_left_x(main_bullet), canvas.get_top_y(main_bullet))
        if collided_object and collided_object == green_hitboxx:
            canvas.delete(green_hitboxx)
            level5(canvas,score)
            break
        if collided_object and collided_object == red_hitboxx:
            canvas.move(green_hitboxx,-45,0)
        if collided_object and collided_object == blau_hitboxx:
            canvas.move(red_hitboxx,50,50)
            canvas.move(green_hitboxx,50,50)
        if canvas.get_left_x(green_hitboxx) <= 75 or canvas.get_left_x(red_hitboxx) <= 0:
            canvas.delete_all()
            GAMEOVERSCREEN(canvas,score)
            break
        ghw1 = -1.8
        ghw2 = -1.8
        hiz = random.randint(-25,-1)
        canvas.move(green_hitboxx, hiz, ghw1)
        hiz = random.randint(-15,-1)
        canvas.move(red_hitboxx,hiz,ghw2)
        hiz = random.randint(-15,-1)
        canvas.move(blau_hitboxx,hiz,ghw2)
        if canvas.get_top_y(green_hitboxx) + 60 > 400 or canvas.get_top_y(green_hitboxx) <100:
            ghw1 = - ghw1
        if canvas.get_top_y(red_hitboxx) + 60 >=400 or canvas.get_top_y(red_hitboxx) <100:
            ghw2 = - ghw2
            
        canvas.update()
        time.sleep(0.02)
        
def level5(canvas,score):
    canvas.delete_all()
    main_ground(canvas)
    clouds(canvas)
    score_label = add_score_label(canvas, score)
    canvas.update()
    gun_man = canvas.create_rectangle(0,0,50,100)
    canvas.set_fill_color(gun_man, 'red')
    canvas.moveto(gun_man,0,400)
    main_bullet = canvas.create_oval(50,canvas.get_mouse_y(),75,canvas.get_mouse_y()+25)
    canvas.set_fill_color(main_bullet,canvas.get_random_color())
    canvas.move(main_bullet, 0,200)
    # ----------------------------------------------------------------------- LEVEL 1
    RANDOM_SIZE = random.randint(30, 75)
    RANDOM_Y = random.randint(150,225)
    red_hitboxx = canvas.create_oval(750,RANDOM_Y,800,RANDOM_Y+RANDOM_SIZE)
    RANDOM_SIZE = random.randint(30, 50)
    RANDOM_Y = random.randint(300, 350)
    blau_hitboxx = canvas.create_oval(750,RANDOM_Y,800,RANDOM_Y+RANDOM_SIZE)
    RANDOM_SIZE = random.randint(30, 80)
    RANDOM_Y = random.randint(400, 450)
    green_hitboxx = canvas.create_oval(750,RANDOM_Y,800,RANDOM_Y+RANDOM_SIZE)
    canvas.set_fill_color(blau_hitboxx,'blue')
    canvas.set_fill_color(red_hitboxx, 'red')
    canvas.set_fill_color(green_hitboxx, 'green')
    # --------------------------------------------------------------------
    
    while True:
        mouse_y = canvas.get_mouse_y()
        clicks = canvas.get_new_mouse_clicks()
        if mouse_y > 75 and mouse_y < 400:
            canvas.moveto(gun_man, 0,mouse_y)
        if mouse_y > 75 and mouse_y < 400 and canvas.get_left_x(main_bullet) < 80:
            canvas.moveto(main_bullet, 50, mouse_y+35)
        if canvas.get_left_x(main_bullet) > 60 and canvas.get_left_x(main_bullet) < 800:
            canvas.move(main_bullet, 20, 0)
        elif canvas.get_left_x(main_bullet) >= 800:
            canvas.moveto(main_bullet, 50, mouse_y+35)
        if clicks and canvas.get_left_x(main_bullet) < 60:
            canvas.move(main_bullet, 30, 0)
        collided_object = canvas.find_element_at(canvas.get_left_x(main_bullet), canvas.get_top_y(main_bullet))
        if collided_object and collided_object == green_hitboxx:
            canvas.delete(green_hitboxx)
            level2(canvas,score)
            break
        if collided_object and collided_object == red_hitboxx:
            canvas.move(green_hitboxx,-45,0)
        if collided_object and collided_object == blau_hitboxx:
            canvas.move(red_hitboxx,50,50)
            canvas.move(green_hitboxx,50,50)
        if canvas.get_left_x(green_hitboxx) <= 75 or canvas.get_left_x(red_hitboxx) <= 0:
            canvas.delete_all()
            GAMEOVERSCREEN(canvas,score)
            break
        ghw1 = -1.9
        ghw2 = -1.9
        hiz = random.randint(-7,-3)
        canvas.move(green_hitboxx, hiz, ghw1)
        hiz = random.randint(-7,-3)
        canvas.move(red_hitboxx,hiz,ghw2)
        hiz = random.randint(-7,-3)
        canvas.move(blau_hitboxx,hiz,ghw2)
        if canvas.get_top_y(green_hitboxx) + 60 > 400 or canvas.get_top_y(green_hitboxx) <100:
            ghw1 = - ghw1
        if canvas.get_top_y(red_hitboxx) + 60 >=400 or canvas.get_top_y(red_hitboxx) <100:
            ghw2 = - ghw2
            
        canvas.update()
        time.sleep(0.02)
        

# ---------------------------------------


# DONT FORGET CANVAS.UPDATE


def main():
    canvas = Canvas(800,600)
    canvas.set_canvas_title("GUNGUY")
    canvas.set_canvas_background_color('SkyBlue1')
    score = 0
    starting_screen(canvas,score)
    
        








    canvas.update()
    time.sleep(0.02)
            

    canvas.mainloop()


if __name__ == "__main__":
    main()
