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
def his_dad_talk(w: World):
    who = w.get("who")
    return w.scene('$shotaの父の話',
            w.symbol("　　　　◆"),
            who.do("通されたのは応接間だった"),
            who.do("中庭に面していて、本棚やゴルフのトロフィーなんかが飾られたガラス棚がある。革製のソファは見た目ほど硬くはなくて、座ると私の下半身が軽く沈んでそこに吸い付いたみたいになった"),
            who.do("棚にはトロフィー以外にも小さなクマのぬいぐるみや、古い家族写真がある。黄色い帽子を被った小さな彼と父親、少し離れて母親が一緒に写っている。保育園か幼稚園の遠足だろうか。幸せそうに笑っている彼が少し羨ましい"),
            who.talk("珈琲が良かったかな？"),
            who.talk("あ、いえ。お構いなく"),
            who.do("ポロシャツ姿の彼は小さなお盆に持ってきたお茶の入ったコップを私の前に置いた。立ち姿はすっと背筋が伸びていてスタイルが良く、ジーンズすら高級品に見える。大きくなったら翔太郎もこんな風になっていたのだろうかと想像してしまう。ただ父親の方が彼よりも背が高く骨格もがっちりしているので、ひょっとしたら翔太郎は母親似なのかも知れない"),
            who.talk("今日子さんだったかな"),
            who.talk("はい"),
            who.do("ガラステーブルを挟んで対面に座ると、彼は私の顔を確かめるようにじっと見つめた"),
            who.talk("あの？"),
            who.talk("いや、女の方が訪ねてこられたのは初めてなのでね。その、翔太郎とは小学校で？"),
            who.talk("その……"),
            who.do("適当を言って誤魔化すことも可能だったけれど、私は正直に打ち明けることを選んだ。それがどんなにおかしなことだと笑われても、私にとっての翔太郎はあの時間の中にしかいないから"),
            who.talk("……そうですか"),
            who.do("私が大きくなった彼と会って話したり、結婚の約束をしていたと言われたりしたと語ると、彼は大きく溜息をついてから、考え込むようにテーブルを見つめた"),
            who.talk("私にもそれが本当のことだったのかどうか、よく分かりません。ただ、私には記憶が思い出せない頃があって、もしその時に彼と本当に結婚の約束をしていたんだとしたら、何かそういう不思議な縁みたいなものが、会わせてくれたのかなって"),
            who.talk("ちょっとだけ待って下さい"),
            who.do("そう言って彼は立ち上がると、私を部屋に残して出て行ってしまう"),
            who.do("やはり不快にさせたのだろうか、と思ったが、暫《しばら》くすると彼はその手にアルバムを持って戻ってきた"),
            who.talk("見て下さい"),
            who.do("私はそこに彼の幼少期の愛らしい姿が写り込んでいるものと思って目を向けたが、開かれたページにあった写真はどれも病室のそれだった"),
            who.talk("これは？"),
            who.talk("翔太郎が亡くなる一週間から半年ほど前までのものです。あの子は脳腫瘍でこの世を去りました。今月の十日が、あの子の命日でした"),
            who.do("それは私が翔太郎に連れられてホテルに行ったあの日だった"),
            )

