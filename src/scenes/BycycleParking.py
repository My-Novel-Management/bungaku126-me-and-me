# -*- coding: utf-8 -*-
'''
Stage: "stage name"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def rain_friend_a_man(w: World):
    kyo = w.get("kyoko")
    sachi = w.get("sachi")
    return w.scene('雨と傘と男',
            w.cmd.change_stage("BycycleParking"),
            kyo.talk("何でなのよ……"),
            kyo.do("急に振り出した雨は私の肩まで伸びた髪をしっかりと濡らして雫を大量に滴《したた》らせる。駐輪場は屋根付きで心底良かったと思うけれど、正直一度帰って着替えてきたい気分だ"),
            kyo.do("私は鞄からハンドタオルを出して、何とか髪の上辺の水分と冷たくなったシャツの肩なんかを拭《ぬぐ》うが、とてもそれで何とかなるような濡れ方ではなかった"),
            kyo.do("他の生徒も同様に文句を言いながら自転車で入ってきたけれど、中にはどこかで拾ったんじゃないかと思うような骨の折れたビニール傘で何とか一時しのぎをしているように見える男性もいる"),
            kyo.do("彼は私を一瞬だけ見たが、すぐにそのまま講義棟の方へと駆けて行ってしまった"),
            kyo.do("私は籠から鞄を引っ張り出して一度天を見上げる。雨は少し弱まったけれど、もうちょっとだけ濡れる覚悟が必要かも知れない"),
            kyo.do("心の中で「よし」と合図して駆け出そうとしたところで、声を掛けられた"),
            kyo.do("赤と白の市松模様をした傘を持った友人が、小さく手を挙げてこちらに近づいてくる"),
            sachi.talk("入ってく？"),
            kyo.talk("助かります"),
            kyo.do("三十度の深いお辞儀をしてから顔を上げ、互いの顔を見合わせると気の置けない笑顔になる"),
            kyo.do("私は砂山幸子の傘の下をおすそ分けしてもらうと、彼女が話し出した昨夜のドラマの話に適当に相槌を打ちながら歩き出した"),
            )

