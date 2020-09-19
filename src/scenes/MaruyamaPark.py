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
def cleaning_volunteer(w: World):
    kyo = w.get("kyoko")
    matsu, saito = w.get("matsu"), w.get("saito")
    sachi = w.get("sachi")
    kunugi = w.get("kunugi")
    return w.scene('清掃ボランティア',
            w.cmd.change_stage("MaruyamaPark"),
            kyo.do("休日の円山公園には一週間ぶりの日差しの所為《せい》か、人が多い"),
            kyo.do("私は病み上がりの中、何とか風邪薬を飲み、マスク姿で幸子たちの後ろの木陰に立っていた"),
            sachi.talk("別に休んでも良かったのにさ"),
            kyo.talk("倒れるほどじゃないから"),
            kyo.do("砂山幸子は心配そうに私を見たけれど、ゴミ袋と火バサミを持って現れた椚木《くぬぎ》先輩たちの姿に緊張気味に頭を下げた"),
            sachi.talk("おはようございます、先輩"),
            kunugi.talk("おはよう砂山。みんな来てる？"),
            kyo.do("先輩は人差し指を立てて人数を確認しているが、足りなかったのか周囲をきょろきょろとする"),
            kyo.do("幸子はブルーのショートパンツにオレンジのパーカーという、どう見ても軽いレジャーに参加しますという格好だけれど、先輩たちも私も下はズボンで上も薄手の長袖のシャツといった地味な服装だ。それでも椚木先輩だけは何だかそれが様になって見える。体型なのか立ち姿なのか、ちょっとした仕草も決まっていて、やはり憧れが湧いてくる"),
            kunugi.talk("あと二人だね……ああ、こっちだよ松本"),
            kyo.do("大きく手を振った先輩の視線の先を振り返ると、黒のタンクトップを着た大男と、その三歩ほど後ろにちんまりと俯いて歩いてくる二人の姿が見えた。一人は確かに松本だったが、もう一人、暑そうな白のふわりとしたブラウスを羽織ったデニム地のロングスカートの眼鏡の女性は、どうやら私のよく知る人物らしい"),
            kyo.do("こちらに気づくと表情をぱっと明るくして、小走りになって松本を追い抜いてやって来る"),
            saito.talk("来ちゃった、岩根さん"),
            kyo.talk("斉藤さん……どうして？"),
            kyo.do("小息を切らせて私の右隣まできて腕を取ると、彼女は悪びれた風もなく「同じサークルに入ったの」と答える"),
            kyo.do("その言葉に幸子は「だれ？」と目線を投げて寄越したけれど、私は彼女のことを説明する気力がどうしても湧かず、ただ曖昧な苦笑を返した"),
            kunugi.talk("あ、そうそう。彼女、斉藤三紀さんだけど、我がカンポカに入部してくれることとなりました。拍手"),
            kyo.do("紹介の声の大きさに顔を赤くして俯きながらも彼女は、私の隣で疎らな拍手を受ける"),
            kunugi.talk("自己紹介はまた次の例会でやるとして、今日はそうね……岩根と一緒に活動して"),
            saito.talk("は、はい。分かりました"),
            kyo.do("宜しくね、と小声で付け加えて私に会釈をする斉藤さんに色々と尋ねたいことがあったが、椚木先輩たちが班分けをし始めたので、黙ったままその動向を見守った"),
            kunugi.talk("それじゃあ岩根と斉藤さん、それにあと松本。その三人で東側回ってきて"),
            kyo.talk("……はい"),
            kyo.do("椚木先輩からゴミ袋と火バサミを受け取りながら、内心ではどうして松本なのだろうと文句がもたげた"),
            matsu.talk("あの"),
            kunugi.talk("何だ松本？"),
            matsu.talk("不慣れな俺と斉藤さんのお守りを病み上がりの彼女に任せるの、流石にアレなんじゃないすかね"),
            kyo.do("普段なら誰も口答えしようとしない椚木先輩に対して臆することなく言った彼の、ちょんと伸びた顎髭が何だか逞《たくま》しく見える"),
            kunugi.talk("良い着眼点だな松本。だが女性ばかりになるより男性が混ざっていた方が色々と面倒なことがない。そうでなくとも二人とも声掛けられ易そうなタイプなんだから、強面一人つけるのは当然だろう？"),
            kyo.do("先輩に言われると説得力がある"),
            kyo.do("ただ強面と言われた当の本人は私たちを見てから自分を指差して沈黙の抗議をしていた"),
            kunugi.talk("それじゃあ一時間後に再びここに集合ね。何かあればＬＩＮＥに……岩根たちは電話でもいいけど、松本に連絡係やらせてもいいよ"),
            kyo.do("はいはい、といった体で彼は頭を掻く素振りを見せると、私と目線が合って何故か軽く会釈をした。よろしく、の意だろうか"),
            saito.talk("けど良かったあ"),
            kyo.do("先輩の「開始」という声でバラバラと班に分かれて歩き出すと、すぐに斉藤さんが隣にやってきて安堵の息を漏らす"),
            kyo.talk("よく私が環境保全同好会だって知ってましたね"),
            saito.talk("教えてくれたの岩根さんだよ？　だって昨日話してくれたじゃない？"),
            kyo.do("え？"),
            saito.talk("だからわたし、思い切って椚木さんに連絡して今日入れてもらった訳だし"),
            kyo.do("彼女が嘘を言っているようには見えなかったから、私は余計に混乱する。昨日は風邪で寝込んでいたから覚えていないだけだろうか"),
            kyo.do("私は携帯電話を取り出して、慌てて履歴を確認する"),
            matsu.talk("なあ。それって俺が持った方がいいよな？"),
            kyo.talk("それ？"),
            kyo.do("急に頭の上から低い声がして驚いたけれど、松本がすっと手を出して私からゴミ袋と火バサミを取ってくれた"),
            kyo.talk("ありがとう"),
            kyo.do("おう。ただそれだけを返して私と斉藤さんの前に出ると、彼は一人で足元のゴミを拾いながら歩いていく"),
            kyo.do("私は途中だった電話の確認をしてそこに斉藤さんからの着信履歴があるのを見つけると、立ち止まって空を見上げた。真っ白だ。雲が広がっている"),
            saito.talk("どうかした？"),
            kyo.do("いつまでも歩き出さない私に当の斉藤さんが声を掛ける。彼女に視線を向けた私は軽く首を横に振ると、一人でゴミ拾いをしながら進んでいく大男の背中を小走りで追いかけた"),
            )


def matsumoto_and_saito(w: World):
    kyo = w.get("kyoko")
    matsu, saito = w.get("matsu"), w.get("saito")
    return w.scene("$matsuと$saitoさんと",
            w.cmd.change_stage("MaruyamaPark"),
            kyo.do("何度か円山公園のゴミ拾いに参加しているけれど、この日はいつもに比べて空き缶やお菓子のゴミ、ビニール袋などの戦利品が少なかった"),
            kyo.talk("結構歩いたけど、どうする？"),
            kyo.do("木陰に入ったところで松本が私たちを見下ろして尋ねた。その表情に「もう十分だろ？」という気分を感じ取ったけれど、時間にしてまだ三十分も経っていない"),
            saito.talk("暑くなってきましたね"),
            kyo.do("なら離れてくれればいいのに、と思う斉藤さんはずっと私の傍で、今は左の肩を私の右肩に付けている"),
            kyo.do("幸子も一緒ならたぶん松本の意見に賛成していただろうけれど、椚木先輩は意外ときっちりしているから、ゴミ袋をもう少し太らせないといけないだろうな、という考えが巡る"),
            matsu.talk("ちょっとだけ、これ頼むわ"),
            kyo.talk("え？"),
            kyo.do("そう言って松本はゴミ袋を渡すと、一人で勝手に駆けて行ってしまう"),
            saito.talk("トイレかな？"),
            kyo.do("冗談ではないのだろうけれど、真顔でそう尋ねた斉藤さんがおかしくて、何だか吹き出してしまった"),
            saito.talk("え？　何かまた変なこと言ってる？"),
            kyo.talk("ううん。大丈夫ですよ。それよりちょっと休憩いれましょう"),
            kyo.do("私は足元が濡れていないことを確認して腰を下ろす。斉藤さんもそれに倣って座ったが、彼女はわざわざハンカチを取り出してそれを自分の下に敷いた"),
            saito.talk("やっぱり変？"),
            kyo.talk("ううん。全然そんなことないです。寧ろ自分の方が気にしてないんだなと思って"),
            kyo.do("フォローのつもりではなくそう言ったのだが、斉藤さんは気にしたようで、三角座りで膝を抱え込むと、そこに顎を沈めた"),
            saito.talk("いつもなの"),
            kyo.do("彼女は足元を見つめたまま言った"),
            saito.talk("他人のことを気にして行動してるつもりなんだけど、どこかズレてるみたいで、クスクスって笑われて、なんか悪いことしているんだって気分になって、適当な愛想笑いして、そっと逃げ出すんです"),
            kyo.do("斉藤さんは私の方を見ずにそのまま話す。相槌も待たないし、それどころかどう思うのかを耳に入れたくないみたいに、小さな声で言葉を並べた"),
            saito.talk("最初はね、ちゃんとどこが悪くてどこがおかしくて笑うのか、いちいち聞き返してたんですよ？　でもそのうちに相手が答えてくれなくなって、最終的に『ごめん』って謝られちゃうんです。けどそれってたぶんわたしの方が悪くて、そんな風にしているうちに段々わたしってみんなから避けられているのかなって思うようになって"),
            kyo.do("彼女の話のはずなのに、まるで自分の学生時代を告白されている気分になる。私もまた周囲とうまく距離感が掴めず、集団からいつも少し離れてぽつんと一人でいる方だった"),
            saito.talk("だからいつの間にか誰とも喋らなくなったし、誘われても行かなくなったし、誰かと一緒にいたいと思うこともなくなった。一人いる方が何も気にしなくていいから楽なんだなって分かってからは、わたしにとって友だちは本や漫画だった。そういうのを暗いって言われるんだったらもうわたしは暗い子ちゃんでいいし、でも誰かと関わり合いにならないなら、そんな風に何か言われることすらないんだなって"),
            kyo.talk("斉藤さん"),
            saito.talk("あ……ごめんなさい。わたしったらまた"),
            kyo.do("私はそっと手を伸ばして、彼女の膝を押さえている手に重ねる"),
            kyo.talk("大丈夫ですよ。何もおかしなことなんて言ってませんから。それより、好きな本とか漫画とか、食べ物とか。友だちと話したかったことを、私と話しませんか？"),
            kyo.do("彼女はやっと私に顔を向けたけれど、その目には大粒の涙が光っていて、見ているうちにぽろりとその一粒が落ちていった"),
            saito.talk("わたし、岩根さんと友だちになれて、良かったです"),
            kyo.talk("おーい"),
            kyo.do("私が斉藤さんにハンカチを出して渡そうとしたところで、松本が戻ってくる。その手には三本のペットボトルが抱えられていた"),
            matsu.talk("オレンジとリンゴとお茶、好きなのどうぞ"),
            kyo.talk("買ってきてくれたんですか？"),
            kyo.do("そうだが、と不思議そうな顔をする彼から私はオレンジを、斉藤さんはリンゴを貰って、そのひんやりとしたボトルを両手で抱いた"),
            matsu.talk("その……俺っていつも間が悪いっつーか、どうもＫＹってやつなんすよ"),
            kyo.talk("松本さんがＫＹ？"),
            matsu.talk("知らないすか？　空気読めとか何とかっての"),
            kyo.do("私は斉藤さんと顔を見合わせて笑う。口元こそ押さえたけれど、笑い声までは隠せなかった"),
            matsu.talk("何か変すか？　けど斉藤さんと深刻っぽい話してたんじゃないんすか？"),
            kyo.do("堀の深い顔が困惑で歪《ゆが》む。でもその歪んだ眉がおかしくて、やっぱりまた笑ってしまう"),
            kyo.talk("斉藤さんも私も松本さんのことそんな風に思ってませんよ。それに深刻なことを話してた訳じゃなくて、ちょっとした昔の思い出話で泣いちゃってただけだから。ですよね？"),
            saito.talk("うん。そう。ありがとう"),
            kyo.do("松本は相変わらず分からないといった表情のままだが、それでもお茶のボトルキャップを外して豪快に喉を鳴らすと、私の足元に置いたゴミ袋を持ってくれた"),
            kyo.talk("そういえば松本さんて彼女持ちなんですよね？"),
            kyo.do("背を向けて芝生の上を駆けている子供たちを見やる彼に、私は思い切って尋ねてみる"),
            matsu.talk("ええ、いますよ。同棲中です"),
            kyo.talk("そ、そうなんだ……"),
            kyo.do("やはりこの手の話題が好きなのか、斉藤さんは頬の色を少し変えて松本を見上げた"),
            kyo.talk("その彼女とはさ、結婚とか考えたりしているんですか？"),
            saito.talk("ちょっと岩根さん、そんな大胆な"),
            matsu.talk("結婚はちょっとできないすね"),
            kyo.do("考える素振りもなく即答すると、彼は再びお茶を飲む"),
            kyo.talk("そうですよね。まだ若いし"),
            matsu.talk("いや、そういうんじゃなくて……まあ色々事情があるんで"),
            kyo.do("明らかに斉藤さんの表情が変わった。私を見て、もっと訊いてとばかりに腕を小突く"),
            kyo.do("けれどわざわざ言葉を濁したところをみると、無理やり聞き出すのは躊躇《ためら》われた"),
            kyo.do("私はキャップを捻り、オレンジ果汁十パーセントの砂糖水を流し込む。斉藤さんもそれに倣ったのか、既に開けていたリンゴジュースを飲んだが、私の顔を覗き込んでから何度か目線を彼の筋肉質で大きな背中へと向ける"),
            kyo.talk("松本さんて高校までは何か部活してたんですか？"),
            matsu.talk("高校はやってないです。中学まではバスケでしたけど"),
            kyo.do("彼はそれに答えるのもこちらには一切表情を見せないままで、それがわざとなのかどうなのか、私には判断が付かなかった。それでも他人に踏み込んで欲しくない一線を彼も持っているんだと感じて、私の抱いていた松本亘という人物への印象は大きく変わった"),
            )
