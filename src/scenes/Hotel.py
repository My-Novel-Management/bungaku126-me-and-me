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
def shota_and_hotel(w: World):
    kyo = w.get("kyoko")
    sho = w.get("shota")
    return w.scene('$shotaとホテル',
            w.cmd.change_stage("Hotel"),
            w.cmd.change_time("night"),
            kyo.be(),
            sho.be(),
            kyo.talk("翔太郎？　ねえ帰ろう？　せめて私のアパートで"),
            kyo.do("何なのだろう。自分のアパートなら良いのだろうか"),
            kyo.do("初めて入った男女がそういうことをする所謂ラブホテルみたいな場所はどこに目を向けていいのやら分からず、$Mはただ彼に手を引かれるままにエレベータに乗って三階で降りた"),
            kyo.do("部屋に入るとドアが閉められ、間接照明になっているところに置かれた巨大なベッドに彼だけが寝転がった"),
            kyo.talk("一体何のつもり？"),
            kyo.do("やっと解放された自分の左手を擦りながら天井を見上げて大の字になっている彼に尋ねる"),
            kyo.talk("もし明日消えるとしたら、今日子にボクを忘れないでいてもらう為の方法って、こういうことしかないんじゃないかって思うんだ"),
            kyo.talk("明日消えるの？"),
            kyo.do("引っ越したりするのだろうか", "&"),
            kyo.do("けれど彼は私の問いには答えず手招きをする"),
            sho.talk("今日子もここにきて天井見てみなよ。面白い"),
            kyo.talk("天井ならここからだって見られる"),
            kyo.do("そう言って顎を上げたところで私の腕が引っ張られた",
                "ベッドに顔から突っ込んだが布団の感触が想像以上に柔らかくて少しだけ良い匂いがした"),
            sho.talk("今日子"),
            kyo.do("上を向いた私に、彼が馬乗りになる"),
            kyo.talk("翔太郎……やめて"),
            kyo.do("彼の腕が両肩を押さえ込んでじっと見つめる小動物の瞳が、潤んでいた",
                "その彼の後側に薄っすらと沢山の星が見えて何だか急に切なくなる"),
            sho.talk("まだ、思い出さない？"),
            kyo.do("涙の混ざった声は、いつもより子供っぽい"),
            kyo.talk("ごめんなさい。でも本当にあなたと結婚の約束をしていたとしても、今の私じゃ結婚をしてあげられないわ。誰か他人との生活を受け入れられるほど、強くないから"),
            sho.talk("今日子じゃなきゃ、駄目なんだ"),
            kyo.talk("それでも……ごめん"),
            kyo.do("彼の頭が私の胸元に落ちてくる"),
            kyo.talk("ねえ！？"),
            sho.talk("ちょっとだけ……このまま"),
            kyo.do("啜り泣きを始めた彼はそう言うと私の背中に腕を伸ばして思い切り抱きついた",
                "でもそれが全然不快に感じなくて、寧ろ私は自分の胸元で泣いている生き物を愛おしいと思って、柔らかなマッシュルームの髪を抱き締めた"),
            kyo.do("自分じゃない誰かを、抱き締める"),
            kyo.do("ただそれだけの行為がこんなにも自分を安心させてくれることをこの日初めて私は知った"),
            kyo.do("彼はそれ以上何も言わず、私もそれ以上何も尋ねず、いつの間にか消えた間接照明は天井に夏の大三角をくっきりと映し出してくれた"),
            kyo.do("星空がこんなに近くに見える"),
            kyo.do("そう感じた刹那、私の意識は隙間の闇に吸い込まれるようにして途切れてしまった"),
            w.symbol("　　　　◆"),
            kyo.do("自分の胸の上の軽さに驚いて、私は目を開く"),
            kyo.do("まだ天井には星座がゆっくりと動きながら映し出されていたけれどカーテンの外は既に明るくなっているのが分かった"),
            kyo.talk("え……あれ……"),
            kyo.do("部屋には彼の姿はなく私は裸になることもないままラブホテルのベッドの上で一夜を過ごしたのだと気づいて、起き上がった"),
            )

