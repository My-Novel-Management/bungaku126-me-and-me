# -*- cofing: utf-8 -*-
'''
Stage: xxx
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def ch1(w: World):
    who = w.get("who")
    return w.scene("# 第１話　私とワタシ",
            )

def ch2(w: World):
    who = w.get("who")
    return w.scene("# 第２話　私と彼",
            )

def ch3(w: World):
    who = w.get("who")
    return w.scene("# 第３話　私とわたしたち",
            )

def ch4(w: World):
    who = w.get("who")
    return w.scene("# 第４話　私と父",
            )

def ch5(w: World):
    who = w.get("who")
    return w.scene("# 第５話　私とわたし",
            )


