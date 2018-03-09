# -*- coding: utf-8 -*-
from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"

    next = raw_input("> ")
    # 判断键入值是否为数字
    # if "0" in next or "1" in next:
    # if int(next):
    if next.isdigit():
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")  # 'type a number': '键入数字'

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."  # 'a bunch of': '一群，一堆'
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")  # 'slaps': '打了'
        elif next == "taunt bear" and not bear_moved:  # 'taunt': '嘲讽'
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")  # 'pissed off': '生气'
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthu1hu_room():
    print "Here you see the great evil Cthu1hu."
    print "He, it, whatever stares at you and you go insane."  # 'stare': '凝视', 'insane': '疯狂的'
    print "Do you flee for your life or eat your head?"  # 'flee': '逃离'

    next = raw_input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")  # 'tasty': '美味的'
    else:
        cthu1hu_room()


def dead(why):
    print why, "Good job!"
    exit(0)


def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthu1hu_room()
    else:
        dead("You stumble around the room until you starve.")  # 'stumble': '跌倒', 'starve': '饿死'

start()
