#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: "title"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from storybuilder.assets import common_rubi
from config import ASSET
# import scenes
from scenes import Stage


################################################################
#
#   1. Initialize
#   2. Story memo
#   3. Structure    - 1/8
#   4. Spec
#   5. Plot         - 1/4
#   6. Scenes
#   7. Conte        - 1/2
#   8. Layout
#   9. Draft        - 1/1
#
################################################################

# Constant
TITLE = "わたしとワタシと私と"
MAJOR, MINOR, MICRO = 1, 0, 0
COPY = "誰かとの付き合い方の悩みとは、結局自分自身との付き合い方なのかも知れない"
ONELINE = "約5万字の青春文学。小さなワタシたちと暮らす大学生の彼女の日常は、ある青年との出会いで崩れていく"
OUTLINE = "約5万字の青春文学。大学生の今日子は他人には見えないＩＦ、イマジナリーフレンドと一緒に暮らしていた。ある日出会った彼女と約束をしたという青年には何故か彼女たちが見え、その日から彼女の日常が歪んでいく"
THEME = "他人との付き合い方"
GENRE = "ジャンル"
TARGET = "20-40years"
SIZE = "70-150枚（210K-450K）"
CONTEST_INFO = "文學界新人賞"
CAUTION = ""
NOTE = "エブリスタで氷室冴子青春文学賞に応募した作品のリメイク"
SITES = ["エブリスタ", "小説家になろう", "ノベルアッププラス", "カクヨム"]
TAGS = ["ドラマ", "文学"]
RELEASED = (9, 30, 2020)


# Episodes
def ch_main(w: World):
    return w.chapter('main',
            Stage.ch1(w),
            Stage.ch2(w),
            Stage.ch3(w),
            Stage.ch4(w),
            Stage.ch5(w),
            )

# Notes
def writer_note(w: World):
    return w.writer_note("覚書",
            )

def plot_note(w: World):
    return w.writer_note("プロットメモ",
            )

def chara_note(w: World):
    return w.writer_note("人物メモ",
            )

def stage_note(w: World):
    return w.writer_note("舞台メモ",
            )

def theme_note(w: World):
    return w.writer_note("テーマメモ",
            )

def motif_note(w: World):
    return w.writer_note("モチーフ",
            )


# Main
def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_version(MAJOR, MINOR, MICRO)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(common_rubi.ASSET)
    w.db.set_from_asset(ASSET)
    # spec
    w.config.set_copy(f"{COPY}")
    w.config.set_oneline(f"{ONELINE}")
    w.config.set_outline(f"{OUTLINE}")
    w.config.set_theme(f"{THEME}")
    w.config.set_genre(f"{GENRE}")
    w.config.set_target(f"{TARGET}")
    w.config.set_size(f"{SIZE}")
    w.config.set_contest_info(f"{CONTEST_INFO}")
    w.config.set_caution(f"{CAUTION}")
    w.config.set_note(f"{NOTE}")
    w.config.set_sites(*SITES)
    w.config.set_taginfos(*TAGS)
    w.config.set_released(*RELEASED)
    return w.run(
            writer_note(w),
            plot_note(w),
            chara_note(w),
            stage_note(w),
            theme_note(w),
            motif_note(w),
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

