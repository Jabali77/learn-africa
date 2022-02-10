import turtle
from turtle import Screen
import pandas
import time

screen = Screen()
screen.setup(width=950, height=900)
screen.title("Learn Africa")
image = "africa_image_five.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

#def get_mouse_click_coor(x, y):
#    print(x, y)

#turtle.onscreenclick(get_mouse_click_coor)

#turtle.mainloop()

data = pandas.read_csv("african_countries.csv")
all_countries = data.country.to_list()
languages = data.language.to_list()
guessed_countries = []
guessed_languages = []

"""Timer Code"""
mins = 15
secs = 0
start_time = time.time()
timer_turtle = turtle.Turtle()
timer_turtle.goto(310, 290)
timer_turtle.hideturtle()
timer_turtle.penup()

while mins >= 0:
    timer_turtle.clear()
    timer_turtle.write(str(mins).zfill(2) + ":" + str(secs).zfill(2), font=("arial", 40, "normal"))
    print(str(mins).zfill(2) + ":" + str(secs).zfill(2))
    secs -= 1
    time.sleep(1)

    if secs == -1:
        secs = 59
        mins -= 1


while len(guessed_countries) < 56:

    answer_state = screen.textinput(title=f"{len(guessed_countries)}/50 Countries Correct",
                                prompt="What's another countries name?").title()

    if answer_state == "Exit":
        missing_countries = []
        missing_languages = []
        for i in all_countries:
            if i not in guessed_countries:
                missing_countries.append(i)
        new_data = pandas.DataFrame(missing_countries)
        new_data.to_csv("countries_to_learn.csv")
        for i in languages:
            if i not in guessed_languages:
                missing_languages.append(i)
        language_data = pandas.DataFrame(missing_languages)
        language_data.to_csv("languages_to_learn_about.csv")
    if answer_state in all_countries:
        guessed_countries.append(answer_state)
        kasa = turtle.Turtle()
        kasa.hideturtle()
        kasa.penup()
        country_data = data[data.country == answer_state]
        kasa.goto(int(country_data.x), int(country_data.y))
        kasa.write(answer_state)
        name_a_language = screen.textinput(title="Language", prompt="Name the most spoken AFRICAN language").title()
        if name_a_language in languages:
            guessed_languages.append(name_a_language)
            kasa.goto(int(country_data.x - 7), int(country_data.y - 7))
            kasa.write(name_a_language)
            #print(time_limit - int(elapsed_time))




