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
    who = w.get("who")
    return w.scene('定期診察',
            who.talk("それじゃあ、一月ほどの間、ずっと彼女たちＩＦの姿は見えていない訳だね？"),
            who.do("診察室には向日葵《ひまわり》の絵が飾られていて、私はそれを眺めながら三浦先生の質問に答えていく"),
            who.talk("岩根さんが見たという別のＩＦだけれど、彼が現れてから何か大きな変化はありましたか？"),
            who.talk("よく分かりません。私自身はそう変わっていないようにも思いますが、先生から見て何か違いがありますか？"),
            who.do("自分の変化なんて、そう簡単に自覚できるのなら、私はもっと上手く生きられている気がする。大学も、サークルも、仕事も、家族のことも、何もかもが大きな変化なんてない。ただ椚木先輩のように私以外の変化はあったり、斉藤さんみたいに新しい人間関係が生まれたりはしたけれど、それが私自身に大きな影響を与えたとも思えない"),
            who.talk("特別な違いは感じませんが、そうですね"),
            who.do("先生はうっすら伸びた顎髭を撫でてから、眼鏡の目を私に向けていつにない優しい笑みを見せてこう続けた"),
            who.talk("部屋に入ってくる時に、私の目を見てから挨拶をしていました。以前は決して私の目を見ませんでしたから、変化といえば変化でしょうか"),
            who.do("そうなのだろうか。自分では意識したことがなかった。もしそれが誰かの影響だとすれば、いつも真っ直ぐに私を見つめてくれた子犬のような目の彼の所為かも知れない"),
            who.talk("それでは次は三ヶ月後で良いですかね"),
            who.talk("はい。次も宜しくお願いします"),
            who.do("そう答えて頭を軽く下げた私を、何故か先生は驚いた顔で見ていた"),
            )

