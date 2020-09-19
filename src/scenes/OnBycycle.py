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
def about_saito(w: World):
    kyo = w.get("kyoko")
    return w.scene('斉藤さんについて',
            w.cmd.change_stage("OnBycycle"),
            kyo.do("バイトのスケジュールはしっかり確認していたはずだったのに、今日ではなく明日だった。そんな落胆と共に自転車のペダルを踏み込みながら、夕焼けが去った空を見上げる"),
            kyo.do("結局あれから斉藤さんとメールアドレスを交換して、形だけは友だちということになった。少しだけ心が軽いのは彼女も私と同じくガラケーだったことだ。ＬＩＮＥのＩＤ交換を、と笑顔で言い出されることに対していちいち「ガラケーなんで」と返すことに、最近気が重い"),
            kyo.do("ちなみに斉藤さんは少し筋肉質の長身男性が好みらしい。それを聞いてから私の頭の中では松本と並んで歩く彼女の姿を想像してしまい、必死に一人で喋り続ける斉藤さんに呆れつつも隣で適当に相槌を打ってあげている彼を勝手に作り上げて、そんな優しい一面を持っていてくれたら苦手意識も無くなるかも知れない、なんて自分勝手な思いが湧き上がってしまった"),
            )

