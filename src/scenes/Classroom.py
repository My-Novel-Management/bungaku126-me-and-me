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
def univ_student(w: World):
    who = w.get("who")
    return w.scene('大学生',
            who.do("半分ほど開けられた教室の窓から入り込んできた風に左頬がそっと撫《な》でられ、私の意識を黒板の「教育と心理学」などと書かれた文字に向かわせる"),
            who.do("机の上に出した分厚い教育心理学概論の教科書は開いていたページが流れてしまっていて、ずっと同じ調子の先生の声に瞼《まぶた》を閉じられないように注意しながらどこのことを言っているのか探す"),
            who.do("携帯電話に表示されている時刻は四時を回っていたが、最近はこの時間でもびっくりするくらいに温かい日が多い。季節外れの嵐や北海道なのにと前置きをされる猛暑日が、知らない間に日常に置かれていた"),
            who.do("手にした携帯を折り畳もうとしたところで、メールの通知がある。砂山幸子《さやまさちこ》からだ。またサークルの話かと思って見ると、チョコミントの美味しい店を見つけたから一緒に食べに行こう、というお誘いだった"),
            who.do("嫌いじゃないけれど特別好きという訳でもない"),
            who.do("だから積極的に断る理由を見つけられない"),
            who.do("それでも返事をしないまま携帯電話を閉じて鞄に仕舞うと、教科書にぼんやりした視線を一旦戻す"),
            who.do("前の席に座って肩を寄せてこそこそ話している同期生は、大学の前に新しく出来たラーメン屋に行くかどうしようかそれなら同じサークルの男子を誘いたいけれど彼って彼女持ちっぽい、みたいな会話をして、チョークを手にした先生の視線を何度か奪っていたが、そんなことを気にしているのは私くらいなもので、座っている誰の心の中にも「早く時間が終わらないかな」という嘆息があるのだろうなとしか感じられなかった"),
            who.do("無理だって出来る訳ないじゃん、という一段大きな声を上げた前の女子は先生の咳払いを聞いてもくすくす笑いを続ける"),
            who.do("そんな風に誰かのことを気にせず生きていけたら、私はきっと、もう少し孤独になれるのだろうけれど、いつまで経っても周囲の雑音は消えないまま、二十歳という年齢を越してしまった"),
            )


def mushroom(w: World):
    who = w.get("who")
    return w.scene("マッシュルーム",
            who.do("翌週の火曜日だった。一時限目から授業を入れていて、それでもこの日はいつもより早く出掛けられたこともあって、十五分も前に教室に入ることができた"),
            who.do("全部で八十ほど席が並ぶ中、私はいつも後ろの窓際を確保する。窓際が空いていなかったら廊下側。真ん中や前の方は落ち着かない。誰かに見られているかも知れない、という感覚が強くなるからだ"),
            who.do("あの子たちがいない、見えない空間というのは、普通に考えれば私にとってとても落ち着ける空間のはずだった。けれど現実はびくびくと怯えて、つい周囲の人の視線を確認してしまう"),
            who.do("開始時刻が近づくにつれ、教室にも人が増えていくけれど、私を視界に入れて何か表情が変わるような人間はいない"),
            who.do("気にしすぎている、ということは理解していた"),
            who.do("それがまた新しい自分を生み出すかも知れないということも、中学の頃から診《み》てもらっている三浦先生に注意されていた"),
            who.do("常に一緒にいる訳ではないきょう子もキョウコも、本当に私のイマジナリーフレンドなのだろうか。未だに一度として、クリニックの病室に彼女たちが現れたことはなかった"),
            who.do("気を抜くと、授業が始まっていた"),
            who.do("眼鏡を掛けた女性講師が教育と子供の成長について、やたらとカタカナ語を交えて話している"),
            who.do("けれど私の二つ前に座った女子二人組はそんな内容とは全く関係のない雑談を、こそこそと、それでも何とか聞き取れる程度の大きさで行っていた"),
            who.do("先生はそれについていちいち気にしたりはしないようだが、美人な同級生の誰々がストーカーされて大変だとか、私にもその先生にも一切関係なさそうな話題で、それでも時折笑い声を漏らすものだから集中して講義を聞いていられないな、という思いが湧き上がった"),
            who.do("彼女たちは大学に何をしに来ているのだろうか"),
            who.do("ということは思わないけれど、何も文句を言わずに大学の授業料から月々の仕送りから出してくれた新しい父親のことを考えると、私は心の中で小さな溜息を吐き出すしかなくなる"),
            who.do("視野から彼女たちの姿を消したい、という思いで廊下側に視線を向けると、窓から教室を覗き込む一人の男性がいることに気づいた"),
            who.do("松本とは全く違うタイプで、髪の色を染めているのか、濃い栗色のように見える。前髪多めで首裏の辺りが刈り上げになっているので、マッシュルームという印象を抱いたが、くりっとした人形のような大きな瞳は一瞬だけ私に投げかけられ、彼は楽しそうに唇を結んだ"),
            )


def saito_san(w: World):
    who = w.get("who")
    return w.scene("斉藤さん",
            who.do("耳から顎《あご》までしっかりと続くモジャモジャの髭《ひげ》を上下させながら、黒板の前で磯谷《いそや》教授が喉に絡《から》むようなドイツ語の発音を繰り返していた"),
            who.do("私の隣ではペアになっている斉藤《さいとう》さんが教科書と先生を交互ににらめっこしながら、同じように小さく発音を繰り返している。その私の視線に気づくと恥ずかしそうに笑うのだけれど、今日誕生日なんだと言われて年齢を聞くと実は一つ歳上だったという事実が判明して、なんだかバツが悪い"),
            who.talk("ドイツに限らないけどね、語学を学ぶというのは法則や発音、単語を知るということではなくて、文化を知るってことなんだ。ほら、最近は日本に来る外国の人も増えてるけど、ただ観光したいだけでなくて文化を知りたいんだって言ってわざわざ日本語を覚えて訪ねてくれたりする"),
            who.do("周囲の生徒は「また始まったよ」といった感じでスマートフォンを教科書で隠して見始めたりしていたが、彼女は目を輝かせて先生の話を聞いている。大きな眼鏡に真っ黒でしっかりした髪を耳の後ろで括っていて、斉藤さんが頷く度にそれが上下して揺れるのが二つの耳みたいに思えてちょっとだけ愛らしく感じる"),
            who.do("そんな彼女が浪人生とは思わなかったから、「なに？」という悪意のない顔で私を見られるとどう答えていいものか分からなくなる"),
            who.talk("知りたいならまず学ぶことだ。知らないなら、分からないなら、本を開くか、あるいは知っている誰かに尋ねることだ。タテン・シュタット・ヴォルテ。言葉よりも行動をだよ"),
            who.do("先生は黒板に力強く文字を書くと、そう言って教科書の続きに戻った"),
            )