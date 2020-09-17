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
def friend_and_circle(w: World):
    who = w.get("who")
    return w.scene('サークル',
            who.do("この日はしっかり六時限目まで入っていて、最後の英語の講義を終えた後でぼんやりとした眠気と共に教室を出た"),
            who.do("まだ日は高く、午前中に降り続いていた雨がすっかり上がった為か、いつもより空が綺麗な気がする。それでも体はすっかり気だるくて、二十歳を超えた自分から体力というものが日に日に失われていっているような心地になってしまう"),
            who.do("鞄から携帯電話を取り出して時刻だけ確認し、参加すると返事した手前、今日のサークルの会合には顔を出すべきなんだろうな、という諦めにも似た気持ちを思い出した"),
            who.do("講義棟から外に出るとずっと続く並木道の下を生徒が疎らに歩いている"),
            who.do("暫《しばら》く行くとベンチの前に座る幸子と椚木《くぬぎ》先輩の姿を見つけ、私は小走りになって彼女たちの前に向かう。先輩の方は今日も相変わらず上下とも黒のぴったりした服を着ていて、腰に手を当てた立ち姿のパンツのラインがモデルのようだ"),
            who.talk("今日子。今日は３０２だって"),
            who.talk("聞いたよ。あんたの方から参加するって言ってくれたんだって？"),
            who.do("先輩は私の肩に手を掛けて嬉しそうに身を乗り出す。しっかりと化粧された整った顔の長い睫毛《まつげ》の強い瞳にじっと見られると、女性の私でも何だか照れてしまうけれど、何故か先輩は入会当初から私を気に入ってくれていた。特に何かをした、ということはないのだけれど、集会の時には何かと声を掛けてくれる"),
            who.talk("ちょうどその日、用事がなかったもので"),
            who.do("そう答えた私を見て先輩の後ろで幸子が笑いを堪えているように、確かに最初は行く気はなかったのだ"),
            who.talk("あの"),
            who.talk("そういえばもうすぐ彼も来る予定なんだけど"),
            who.do("幸子の視線が右肩を超えたずっと後ろに向けられ、それから「あ」という声で私もそちらを振り返った"),
            who.do("松本亘だ"),
            who.do("首のところから黒い紐が伸びたカーキ色のパーカー姿で、のっそりと会釈をしてぼそり、低い声で挨拶をした"),
            who.talk("松本です。よろしく"),
            who.talk("わたしは砂山でこっちの彼女が岩根今日子"),
            who.talk("なんで私だけフルネームなの？"),
            who.do("けれど彼女は「いいからいいから」と私と松本を向き合わせる。彼とは頭一つ分以上差があるからどうしたって顔を見上げることになるのだけれど、特に彼に照れた様子はなく、それどころかやはり私に対して何か気に入らないことがあるのか、一瞬睨むような表情になってから、すっと視線を逸《そら》して先輩を見た"),
            who.talk("椚木さん。俺、今日はちょっと用事あるんで決まったこと後でＬＩＮＥしといてもらえますか"),
            who.talk("入部そうそうサボるとはなかなか良い根性じゃないか、松本"),
            who.do("椚木先輩は構わずに松本の肩に手を回して舐めるようにその顎《あご》を見上げる"),
            who.talk("いや勘弁して下さいよ。今日は彼女のライブの手伝いしないといけないんすから"),
            who.talk("松本の彼女って軽音部？"),
            who.talk("大学じゃないすよ。普通にバンド組んで歌ってます"),
            who.do("へえ、と声を漏らしたのは幸子だった。先輩はどんな彼女なのかの質問を始めて、彼は困った様子で何とか逃れようとする"),
            who.do("その姿を見ながら「彼女がいる」と堂々と口にできる松本亘という人間が、少しだけ羨ましく感じた"),
            )


def saito_san2(w: World):
    who = w.get("who")
    return w.scene("斉藤さん・その２",
            who.do("宿題のプリントを鞄に仕舞い、席を立つ。今日の授業はこれで終わりだった"),
            who.do("私は人が一気に減った教室で、思い切り両腕を持ち上げて伸びをする。金曜はサークルの集会があるけれど、バイトもあるし、それに昨日のあの宮内翔太郎《みやうちしょうたろう》とかいう男性のことも気になる"),
            who.talk("あの"),
            who.do("鞄を手に部屋を出て行こうとした私の手を、斉藤さんが掴《つか》んだ"),
            who.talk("何ですか？"),
            who.talk("この後授業入ってますか？"),
            who.do("それはいつも彼女が先生を見る時にしているのと同じ眼差しだった"),
            who.do("左右に首を振った私に嬉しそうにすると、彼女は「少しだけ、付き合ってもらってもいいですか？」と断ってから、一緒に教室を出た"),
            who.do("背中にカーキ色のリュックを背負った短い二つ絞りの髪型の斉藤さんは、鈍い群青色のロングスカートを揺らしながら勢いよく歩いていく。私はそれについていくのがやっとで、途中何度か声を掛けられたのだけれど、とても話に答えられるような状況じゃなくて、「うん」とか「ええ」とか相槌《あいづち》を返すので精一杯だった"),
            who.do("誕生日という免罪符があるからなのか、いつもは授業が終わってすぐ別れるだけの存在だった彼女が、違う姿を見せていた"),
            who.talk("岩根さんはさ、その、大学で友だちとかできた？"),
            who.talk("えっと……"),
            who.do("そう言われて浮かんだのは幸子の顔くらいだった"),
            who.talk("まあサークルの知り合いくらいなら"),
            who.talk("そうだよね。わたしってさ、浪人してるからか、その、まだ友だちとかここでいなくて"),
            who.do("やっと右隣に追いついた私にそう言いながら苦笑を向ける。その化粧気の全くない表情は歳上という感じはない。寧《むし》ろ一年生、下手をするとオープンキャンパスにやってきた高校生と言っても通用しそうだ"),
            who.talk("別にいなくても何てことはないんだけど、でも時々困ることもあるんだよね"),
            who.do("それが何だと思う？　という顔を私に見せてから、彼女は横断歩道の向こう側にあるラーメン屋の看板を指差した"),
            who.talk("え……"),
            who.talk("ほら。何て言うか、一人で食べても大丈夫なものと、そうじゃなくて一人で食べると美味しくないものってあるじゃない？"),
            who.talk("それがラーメン？"),
            who.do("斉藤さんは小さく頷くと、信号が変わった道路の上の白線を踏みしめて歩き出す"),
            who.do("全然自分とは感性が違う他人がそこにいるのを感じつつ、私は諦めたように彼女に続いた"),
            )