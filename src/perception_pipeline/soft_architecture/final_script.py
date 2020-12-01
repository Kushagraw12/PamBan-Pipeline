import pandas as pd
from datetime import datetime
import random

def get_boat():
    b = random.randint(0, 5)
    #print(b)
    if b <= 2: 
        return True
    else:
        return False

def check_train(time, train_id):
    now = datetime.now()
    current_time = now.strftime("%H%M")
    for i in time:
        if int(current_time) == i:
            return False
        else:
            return True
    # return False

def stop_boat():
    print("DISPLAYING RED LIGHT TO SIGNAL THE BOATS TO STOP!")
    print("********************************************************************************************")

def go_boat():
    print("DISPLAYING GREEN LIGHT TO SIGNAL THE BOAT TO APPROACH THE BRIDGE")
    print("#############################################################################################")
    print()

def uplift_bridge():
    print("UPLIFTING THE BRIDGE")
    print("#############################################################################################")
    print("DISPLAYING RED SIGNAL FOR TRAINS")
    print("#############################################################################################")
    print()

def get_rear_cam():
    print("GETTING DATA FROM THE REAR CAM")
    print("#############################################################################################")
    print("CHECKING FOR BOAT IN REAR CAM!")
    print("#############################################################################################")
    print("BOAT DETECTED IN THE REAR CAMERA, BOAT HAS SUCCESSFULLY CROSSED THE BRIDGE")
    print("#############################################################################################")
    print("BRIDGES ARE GOOD TO CLOSE DOWN")
    print("#############################################################################################")
    print()

def put_the_bridge_down():
    print("THE BOAT HAS PASSED, PUTTING THE BRIDGE DOWN")
    print("#############################################################################################")
    print("THE BRIDGE IS DOWN, DISPLAYING GREEN SIGNAL TO TRAINS")
    print("#############################################################################################")
    print()

def solve():
    dt = pd.read_csv("TrainSch.csv")
    #print(dt)
    train_id = dt["TRaIN_ID"]
    tim = dt['TIME']
    #print(time)
    print("GETTING BOAT")
    print("#############################################################################################")
    print()
    boat = get_boat()
    if boat:
            print("BOAT DETECTED")
            print("#############################################################################################")
            print()
            print("CHECKING FOR TRAINS")
            print("#############################################################################################")
            if check_train(tim, train_id) == True:
                print("NO TRAIN INCOMING")
                print("#############################################################################################")
                print()
                go_boat()
                uplift_bridge()
                get_rear_cam()
                put_the_bridge_down()
                print("SUCCESS!")
                print(":)")
                print()
            elif check_train(tim, train_id) == False:
                print("TRAIN INCOMING")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print()
                stop_boat()
    else:
            print("NO BOAT DETECTED")
            print("---------------------------------------------------------------------------------------------")
            print("TRAINS ARE GOOD TO GO!")
            print("---------------------------------------------------------------------------------------------")

if __name__ == "__main__":
    print("STARTING")
    print()
    solve()
