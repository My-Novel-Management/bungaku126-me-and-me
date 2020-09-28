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
            kyo.do("バイトがあるから、とラーメンの後の喫茶店は断って$saitoさんと別れた",
                "大学のキャンパスには相変わらず多くの学生が思い思いに小さな集団を形成して楽しげに暇を潰していたけれど、",
                "その中に自分の居場所はやっぱりなさそうだなと感じて$Mは一人駐輪場へと向かった"),
            kyo.do("ラーメンを一緒に食べた記念としてもらった$saitoさんのメールアドレスを登録しながら$lineの$id交換じゃなかったことにほっとしている自分がいる",
                "携帯電話の液晶に映った『$saitoさん』の文字を見るとこれで形式上は友だちということなのだろうか、と考えてしまう"),
            # TODO
            kyo.do("ちなみに斉藤さんは少し筋肉質の長身男性が好みらしい。それを聞いてから私の頭の中では松本と並んで歩く彼女の姿を想像してしまい、必死に一人で喋り続ける斉藤さんに呆れつつも隣で適当に相槌を打ってあげている彼を勝手に作り上げて、そんな優しい一面を持っていてくれたら苦手意識も無くなるかも知れない、なんて自分勝手な思いが湧き上がってしまった"),
            )

