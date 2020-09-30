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
def campany_people(w: World):
    kyo = w.get("kyoko")
    suzu, arase = w.get("suzu"), w.get("arase")
    return w.scene('会社の人々',
            w.cmd.change_stage("DataInc"),
            kyo.be(),
            kyo.do("三階までやってくると『株式会社アクセルリンクス』と書かれていたプレートが貼り付けられたドアが見え、$Mは慎重にノブを回してそれを押し開けた"),
            kyo.talk("こんにちは……"),
            kyo.do("うつむき加減でぼそりとした挨拶をする私に、奥の窓側の席に座ってパソコンで作業中だった鈴森実里だけが小さく手を挙げる", "&"),
            kyo.do("$Mは会釈をして慣れた調子で入り口脇のタイムカードに時刻を記録すると右手側の机の一つに席を取る",
                "既に他のアルバイトの女性が二人作業中だったから音を立てないようにと注意深く足元に荷物を置いてから、",
                "マウスを動かして切り替わった画面で自分のＩＤとパスワードを打ち込んだ"),
            arase.be(),
            suzu.be(),
            arase.talk("おっはよ、今日子ちゃん"),
            kyo.talk("あ、はい。おはようございます"),
            kyo.do("急に肩を叩いて声を掛けてきたのが室長と呼ばれている現場監督の$full_araseだ",
                "堀の深い顔に跳ね返った癖の強い髪から強烈な甘い匂いをさせている",
                "ストライプ柄のスーツがお気に入りで今日はネイビーブルーのそれにオレンジのタイを合わせていた"),
            arase.talk("どう？　大学は順調？"),
            kyo.talk("ええ。あの、今日の分の打ち込み資料はそれですか？"),
            kyo.do("$araseが手に持っているファイルが$Mの本日の担当分だと分かっていたけれど確認の為に敢えて尋ねる"),
            arase.talk("そうそう。あと出来れば、もうひとセット頼みたいんだけど今日時間ある？"),
            kyo.do("最近はいつもこうだ",
                "$Mが仕事に慣れてきたこともあるのだろうけど他のパートの人の分まで作業を回そうとするのだ"),
            kyo.talk("今日は、ちょっと"),
            kyo.do("だから用事がある風を臭わせて何とか滞在時間の延長を防ぐ"),
            arase.talk("そうだよね。今日子ちゃん真面目な学生だもんね。勉強で忙しいよね"),
            kyo.do("荒瀬は資料ファイルを机に置くとぶつぶつと言いながら自分の席に戻って行く",
                "それを鈴森さんが眼鏡の目で咎めるように見ていたが彼は気づいていないようだった", "&"),
            kyo.do("私の視線に気づいた鈴森さんは右の掌をひらひらとやってさっさと仕事するように促すがその表情は私と同じように苦笑を浮かべていた"),
            kyo.do("画面に視線を戻すと作業用ファイルを開いて集計シートの番号を確認する",
                "続いてエクセルのシートをコピーして画面いっぱいに広げると資料の数字を見ながら該当する項目に打ち込んでいく", "&"),
            kyo.do("単純なアンケートのデータ集計作業だった"),
            kyo.do("社員は荒瀬と鈴森さんだけで他に常時作業をしている派遣の人が数名と残りは$Mみたいなパートタイムの人間ばかりだ", "&"),
            kyo.do("基本的に私語もほとんどなく黙々と数字を打ち込んで三時間経過すれば作業が途中でも終わることができる", "&"),
            kyo.do("時給も悪くないし文句を言われることもない", "&"),
            kyo.do("ただ荒瀬室長がやたらと絡んでくることと鈴森さんに気に入られないと仕事がしづらい、というだけで、それなりに満足のいく職場だった"),
            kyo.do("ちら、と$suzuの様子を確認する",
                "前髪を右の眉毛の端あたりできっちりピンで留めているその几帳面さは少しだけ$Mの母親を思い出させた",
                "何事もきっちりと決められたようにこなしていないと駄目な人でそれを自分だけでなく相手にも求めてしまう",
                "結果、周囲の人間は疲れ果てて彼女からは離れていってしまう", "&"),
            kyo.do("私の最初の父親もそうだった"),
            kyo.do("画面にはただ数字が並んでいる",
                "その意味するところなんか考えなくてもとにかく空白を埋めていくだけで誰かの役には立つのだろう",
                "一人の人間の人生というのもそんなものかもしれない"),
            kyo.do("それでも、と少し気になって資料のタイトルを見やると『家族の会話について』と書かれていた"),
            )

