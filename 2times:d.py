from microbit import *
import microbit
import time
import math
import music

interval = 9
times = 1
time_count = True
times = 1
day = 0
hour = 0
minute = 0

#========================Functions================
# define each of the dice images as strings
heart2 = "09090:" \
        "99999:" \
        "99999:" \
        "09990:" \
        "00900"

heart1 = "09090:" \
        "90909:" \
        "90009:" \
        "09090:" \
        "00900"

heart4 = "09090:" \
        "99999:" \
        "99999:" \
        "09990:" \
        "00900"

heart3 = "09090:" \
        "90909:" \
        "90009:" \
        "09090:" \
        "00900"

# convert the strings to microbit images
heart1 = microbit.Image(heart1)
heart2 = microbit.Image(heart2)
heart3 = microbit.Image(heart3)
heart4 = microbit.Image(heart4)


# create a list that contains all of the images
all_heart = [heart2, heart1, heart4, heart3]


#Get feedback function
def fb():
    flag_fb = True
    box_state = 0
    y = -300 #set a initial y value

    while flag_fb:

        y = accelerometer.get_y()
        if box_state == 0:    #initial box state: set box is closed = 0
            display.show("-") #Shows - for testing
            if y <= -700:     #Box is being opened
                box_state = 1 #now box state is set to 1
        elif box_state == 1:   #
            display.show("O") #shows 0 for testing
            if y > -700:      #if close the box
                time.sleep(3) #wait for 2 seconds
                box_state = 2 #now box state is set to 2

        elif box_state == 2:   #if the box was closed
            for d in all_heart:
                microbit.display.show(d)
                time.sleep(1)
            time.sleep(4)     #
            box_state = 0     #state will back to 0
            flag_fb = False
            return box_state

#Store string to e which should be sent and shown on the APP
def play_melody():
    music.play(music.NYAN)

def wait_interval(interval):# return something return shijian as value of sllep function
    sleep_time = interval * 60 * 60 #in min
    return sleep_time

def sum_fun():

    play_melody()
    fb()

################################# Start working and taking medicine #########################

while True:

    if button_a.was_pressed(): #First time, user should press the button
        times == 1
        day == 0
        hour == 0
        minute == 0
        e = ""
        text = ""
        display.show(Image.ALL_CLOCKS)
        display.clear()
        time_count = True

        while time_count:
            for times in range(1,4):  #loop for write data to the file
                if (times % 3 == 1):
                    time.sleep(wait_interval(interval))
                    display.show(Image.ARROW_NW)
                    time.sleep(3)
                    sum_fun()
                    day = int(int(running_time() / (24 * 3600000)) + 1)
                    hour = int((running_time() / 3600000) - ((day - 1) * 24))
                    minute = int((running_time() % 3600000) / (60 * 1000))
                    e = 'Medicine taken: Day{d}, {h}, {m}'.format(d=day, h=hour, m=minute)
                    with open("box_data.txt", "w") as file_object:
                        text = text + e + "\n"
                        file_object.write(text)
                    times += 1
                    display.scroll("9am F")

            #2nd time
                elif (times % 3 == 2):
                    time.sleep(wait_interval(12))
                    display.show(Image.ARROW_NE)
                    time.sleep(3)
                    sum_fun()
                    #day = int((running_time() / 3600000) / 24)
                    day = int(int(running_time() / (24 * 3600000)) + 1)
                    #hour = int((running_time() / 3600000) % 24)
                    hour = int((running_time() / 3600000) - ((day - 1) * 24))
                    minute = int((running_time() % 3600000) / (60 * 1000))
                    '''
                    day = int(((running_time() / 3600000) / 24) + 1)
                    hour = int((running_time() / 3600000) % 24)
                    minute = int((running_time() % 3600000) / (60 * 1000))
                    '''
                    e = 'Medicine taken: Day{d}, {h}, {m}'.format(d=day, h=hour, m=minute)
                    with open("box_data.txt", "w") as file_object:
                        text = text + e + "\n"
                        file_object.write(text)
                    times += 1
                    display.scroll("21pm F")

                else:
                    display.scroll("Good")
                    times = 1
                    time.sleep(wait_interval(3))