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
def thinking_about(w: World):
    kyo = w.get("kyoko")
    asu = w.get("asuko")
    return w.scene('考える、いろいろと',
            w.cmd.change_stage("Library"),
            kyo.do("八月に入り、テスト期間も三日目を迎えていた"),
            kyo.do("図書館には私と同じように一人でレポートや試験勉強をしている生徒が殆どだ"),
            asu.talk("みんな真面目に勉強しているけれど、今やっていることが社会に出て役に立つなんて思っていないし、そもそもが目の前の片付けなきゃいけない問題をこなしている作業でしかない。そう思うでしょ、今日子も"),
            kyo.do("右の肩越しに話しかけてくるのは明日子だ。赤い眼鏡がちらつくのが、何とも集中力を奪っていく"),
            kyo.talk("せめて静かにしておいてもらえない？"),
            kyo.do("小声でそう抗議するけれど、「どうせ誰にも見えないでしょ」と構う気はない"),
            kyo.do("彼女は私の周囲であれこれと話しかけていたが、相手にされないと分かると、他の人の机に出かけていっては後ろから覗き込んだり隣に座ったり、頬を突《つつ》いたりし始める"),
            kyo.talk("ちょっと！"),
            kyo.do("だからつい声を出して立ち上がってしまったが、当然明日子は他の人たちに見えていないので、私は試験でノイローゼ気味の学生にでも見られてしまったかも知れない。そんな一瞥《いちべつ》を幾つも受けて、私は縮こまって頭を下げると、何も弁解せずに鞄にノートを入れて図書館を立ち去った"),
            asu.talk("ねえねえ。なんで勉強やめちゃったの？　他の人のことなんてそんな気にしなくてもいいのに。何も言ってこないならいないのと同じじゃない？"),
            kyo.do("大学の構内を歩きながら、私は何故彼女がここにも現れたのか考えていた"),
            asu.talk("見えててもいないのと同じなら、それこそＩＦみたいなものだよね。ふふ。私たちと同じ。そう考えれば、もっと楽に生きられるんじゃないの？"),
            kyo.do("明日子は私の前に立ち、笑みを消し去った瞳をまっすぐに向ける"),
            kyo.do("それを無視して脇を通り抜けると、ドアを押して外に出た"),
            kyo.do("並木で影ができた道路を自転車が抜けていく。その先を疎《まば》らに学生たちが歩いていたが、別の方向は全く人影がない"),
            kyo.do("携帯電話で時間を確認するとあと三十分ほどで昼になる。空は雨知らずに晴れていて、小さな雲がゆっくりと流れていた"),
            kyo.do("どこか適当な木陰で昼ご飯にしようと歩き出す"),
            asu.talk("無視していればいつかは消えてしまう。もしそうなら、あなたはどうしてきょう子たちを無視しなかったの？"),
            kyo.do("明日子はずっと喋ることをやめない。テスト期間のストレスなのか、それとももっと大きな、そう、家族のことに対する精神的な問題の影響だろうか"),
            kyo.do("今年のお盆も実家には帰らない"),
            kyo.do("そんな心の安寧を決めていた私に、週末、父が会いに来る。出張のついでと言われたが、あまり電話もメールも寄越さず、今年の正月の旭川への帰省も見送ったから、流石に心配になったのだろう"),
            kyo.do("道を離れて木陰を歩いていく"),
            kyo.do("今の父は好い人だ。そう思う"),
            kyo.do("けれど好い人かどうかは私にとってはあまり関係がない。それよりは苦手かどうか、というただ一点が、私をいつも苦しめる"),
            asu.talk("……だからさ、顔合わせすればお小遣《こづか》い貰《もら》えるな、くらいに考えておけばいいのよ。話なんてどうせ大学うまくやってるかとか、そんな当たり障りのないものばかりなんだし"),
            kyo.do("明日子の声は徐々に小さくなっていた"),
            kyo.do("そのうちに彼女の声だけが響くようになり、やがて姿が見えなくなってしまう"),
            kyo.do("振り返った私の首筋を風が抜けていき、完全に彼女がいなくなったことを確認すると、私は木の根元に腰を下ろす"),
            kyo.do("鞄から取り出したおにぎりは、押しつぶされて形が歪んでいた"),
            )

