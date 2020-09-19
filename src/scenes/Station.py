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
def waiting_dad(w: World):
    kyo = w.get("kyoko")
    yukio = w.get("yukio")
    return w.scene('待ち合わせ',
            w.cmd.change_stage("Station"),
            kyo.do("土曜日の札幌駅構内は流石の人の多さで、中には私と同じくらいの学生と思われる集団が大きな荷物を抱えて騒ぎながら待ち合わせをしていた"),
            kyo.do("携帯電話で父親からのメールか電話がないかと確認するが、こっちに来る前に一度メールがあっただけで、それ以降はまだ何も連絡がなかった"),
            kyo.do("時刻は二時を過ぎたところで、予定では到着しているはずだけれど、改札からそれらしき人物が出てくる気配はない"),
            kyo.do("私は今一度、自分の周囲を確認する"),
            kyo.do("明日子はいない"),
            kyo.do("今日の私の格好は白の七部丈のブラウスに紺のロングパンツで、足元はスニーカーだ。けれど彼女はいつもやや露出の多い胸元の開いたシャツや丈の短いスカートを履いた姿で、私の目の前に突然現れる"),
            kyo.do("それは明らかに今までの私のＩＦたちとは違っていた"),
            kyo.do("いつ現れるか分からない彼女に対して常に見張られているような緊張感があり、その為か、最近家に帰っても疲れてそのまま寝てしまうことが増えていた"),
            yukio.talk("今日子さん？"),
            kyo.do("声は後ろからだった"),
            kyo.talk("あ……"),
            kyo.do("振り返ると緑色をしたハーフフレームの眼鏡を掛けたストライプ柄のシャツを着たひょろりとした男性が、鞄を手にして立っていた"),
            kyo.talk("父さん……"),
            kyo.do("まだ昼ご飯を食べていないと言うので、私は彼の後について、お勧めだというスープカレーの店に向かった"),
            )

