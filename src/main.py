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
from scenes import AccelLink
from scenes import Apart
from scenes import AroundStation
from scenes import BycycleParking
from scenes import Classroom
from scenes import Clinic
from scenes import Famires
from scenes import Hotel
from scenes import InTrain
from scenes import KyokoRoom
from scenes import LectureHall
from scenes import Library
from scenes import MaruyamaPark
from scenes import MatsuApart
from scenes import OnBycycle
from scenes import RamenShop
from scenes import ShotaHome
from scenes import ShotaHomeDrawing
from scenes import ShotaRoom
from scenes import SoupCurry
from scenes import Station
from scenes import Street
from scenes import UnivCampus
from scenes import University


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



# Chapters
def ch_me_and_mes(w: World):
    return w.chapter('私とわたしたち',
            w.plot_note("$kyokoはいつも三人分準備する"),
            w.plot_note("$shotaが現れた"),
            w.plot_note("サークルに$matsuが入った"),
            w.plot_note("$kyokoにはIFがいる"),
            "冒頭は朝食の準備シーンから",
            "大学の講堂で主要キャラ出す。マッシュルームは一瞬見えて消えるくらいに",
            "その日にバイト",
            "帰って翔太郎に出会って、１終わりくらいに",
            KyokoRoom.every_morning(w),
            Street.goto_univ(w),
            LectureHall.lecture_IF(w),
            Classroom.mushroom(w).omit(),
            University.friend_and_circle(w),
            AroundStation.goto_work(w),
            AccelLink.campany_people(w),
            Street.meet_mushroom(w),
            Apart.his_introduction(w),
            )


def ch_me_and_life(w: World):
    return w.chapter("私と彼と",
            w.plot_note("$shotaとの約束"),
            w.plot_note("$saitoとラーメン屋に入った"),
            w.plot_note("サークルでゴミ拾い"),
            w.plot_note("$matsuと$saitoと話す"),
            w.plot_note("明日子が現れた"),
            Classroom.saito_san(w),
            University.saito_san2(w),
            RamenShop.ramen_and_girl(w),
            OnBycycle.about_saito(w),
            Apart.shotaro_again(w),
            KyokoRoom.awaking(w),
            KyokoRoom.vanilla_icecream(w),
            KyokoRoom.shotaro_care(w),
            KyokoRoom.awake_and_remember_his_word(w),
            MaruyamaPark.cleaning_volunteer(w),
            MaruyamaPark.matsumoto_and_saito(w),
            Street.asuko(w),
            )


def ch_me_and_family(w: World):
    return w.chapter("私と家族と",
            w.plot_note("出張で札幌にきた父と会った"),
            w.plot_note("$shotaとホテルに入った"),
            w.plot_note("$shotaが消えた"),
            Street.greeting_asuko(w),
            Library.thinking_about(w),
            Station.waiting_dad(w),
            AroundStation.goto_curryshop(w),
            SoupCurry.eating_together(w),
            UnivCampus.about_family(w),
            KyokoRoom.nothing_kyokos(w),
            Famires.shotaro_and_mother(w),
            AroundStation.goto_hotel(w),
            Hotel.shota_and_hotel(w),
            )


def ch_me_and_me(w: World):
    return w.chapter("私と私",
            w.plot_note("サークルの先輩が引退する"),
            w.plot_note("$matsuのIFと出会い、彼が亡くなっていると知った"),
            w.plot_note("$shotaの家にいく"),
            w.plot_note("定期検診"),
            w.plot_note("わたしはわたし"),
            KyokoRoom.alone_days(w),
            Famires.senpai_talk(w),
            MatsuApart.his_girlfriend(w),
            ShotaHome.miyauchi_home(w),
            ShotaHomeDrawing.his_dad_talk(w),
            ShotaRoom.shotaro_and_memory(w),
            InTrain.think_his_family(w),
            Clinic.medical_examination(w),
            Street.me_and_me(w),
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
            #
            ch_me_and_mes(w),
            ch_me_and_life(w),
            ch_me_and_family(w),
            ch_me_and_me(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

