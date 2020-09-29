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
def medical_examination(w: World):
    kyo = w.get("kyoko")
    miura = w.get("miura")
    return w.scene('定期診察',
            w.cmd.change_stage("Clinic"),
            w.cmd.change_time("midmorning"),
            kyo.be(),
            miura.be(),
            miura.talk("それじゃあ、一月ほどの間、ずっと彼女たちＩＦの姿は見えていない訳だね？"),
            kyo.do("診察室には向日葵の絵が飾られていて私はそれを眺めながら三浦先生の質問に答えていく"),
            miura.talk("岩根さんが見たという別のＩＦだけれど、彼が現れてから何か大きな変化はありましたか？"),
            kyo.talk("よく分かりません。私自身はそう変わっていないようにも思いますが、先生から見て何か違いがありますか？"),
            kyo.do("自分の変化なんてそう簡単に自覚できるのなら、私はもっと上手く生きられている気がする",
                "大学も、サークルも、仕事も、家族のことも、何もかもが大きな変化なんてない",
                "ただ椚木先輩のように私以外の変化はあったり、斉藤さんみたいに新しい人間関係が生まれたりはしたけれど、それが私自身に大きな影響を与えたとも思えない"),
            kyo.talk("特別な違いは感じませんが、そうですね"),
            kyo.do("先生はうっすら伸びた顎髭を撫でてから眼鏡の目を私に向けていつにない優しい笑みを見せてこう続けた"),
            miura.talk("部屋に入ってくる時に、私の目を見てから挨拶をしていました。以前は決して私の目を見ませんでしたから、変化といえば変化でしょうか"),
            kyo.do("そうなのだろうか",
                "自分では意識したことがなかった",
                "もしそれが誰かの影響だとすればいつも真っ直ぐに私を見つめてくれた子犬のような目の彼の所為かも知れない"),
            miura.talk("それでは次は三ヶ月後で良いですかね"),
            kyo.talk("はい。次も宜しくお願いします"),
            kyo.do("そう答えて頭を軽く下げた私を何故か先生は驚いた顔で見ていた"),
            )

