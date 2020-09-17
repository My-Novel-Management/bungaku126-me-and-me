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
def town_light(w: World):
    who = w.get("who")
    return w.scene('家路・街の明かり',
            who.do("自転車で路地を駆け抜ける"),
            who.do("段差で少し跳ねて、前の籠に入れた買い物袋の中の生卵のことが気になったけれど、この前のように落とした訳じゃないから大丈夫だろうと思うことにした"),
            who.do("見上げた空は雲が多くて、それでも最近はこの時間もまだまだ明るい。路地の街灯はぼんやりとした光を放ち始め、帰宅途中の学生や会社員をそれとなく照らしている"),
            who.do("この辺りは学生が暮らすアパートが多いけれど、明かりの付いた住宅から漂ってくるのは家庭の夕食の香りだった"),
            who.do("子供たちのはしゃぐ声に、母親の声が重なる"),
            who.do("ちょっと苛立ったやり取りのようだったけれど、それでもどこかごく普通の家庭のそれに思えて、私は腰を上げペダルを漕ぐ足に力を入れた"),
            who.do("ここ最近は暑い日が続いていたが、このくらいの時間帯になればしっとりと空気が落ち着いて、幾分心地良い。風を切って走るこの時間が、私を色々なものから自由にしてくれるような気がして、好きだった"),
            )


def goto_univ(w: World):
    who = w.get("who")
    return w.scene("大学に向かう",
            who.do("自転車で朝の路地を駆け抜ける"),
            who.do("大学までの十分程度の道のりが、私の心をほんの少しだけ解き放ってくれる"),
            who.do("でもそれは天気が良い時に限るというのは、私だけに限定した話じゃないだろう"),
            )


def meet_mushroom(w: World):
    who = w.get("who")
    return w.scene("マッシュルームに出会う",
            who.do("仕事を終えて外に出た時には、すっかり夜の街に様変わりしていた"),
            who.do("会社帰りのサラリーマンの集団や、既に酔っ払っている人の大きな声が路上に響く"),
            who.do("通りにはタクシーが並び、綺麗に着飾った女の人と男性がその一台に乗り込んでいく"),
            who.do("私も将来、あの中の誰かになるのだろうか"),
            who.do("そんなことを考えながら駅へと急いだ"),
            who.do("電車で大学まで戻り、自転車を取りに行って夜道の家路を帰る"),
            who.do("日中の青空の下を駆けるのも心地良かったが、こうして夜風を切るのも悪くない"),
            who.do("それでもアパートが近づくと胃袋の下の方が重くなり始め、彼女たちの存在が自分の中で膨らみ始める。別に何か危害を加えるということはないのだけれど、彼女たちを目にすることで否応なく、自身のトラウマを思い出してしまう"),
            who.do("電信柱に取り付けられた外灯が、嘲《あざけ》るように明滅した"),
            who.do("そこから左に曲がり、アパートの駐輪場へと滑り込む"),
            who.do("普通ＩＦ、つまりイマジナリーフレンドを持つというのはその人物にとっての精神安定剤のようなものらしいが、三浦先生にも指摘されたように、私のように常にアパートにいて一緒に暮らしている他人のように振る舞うというのは珍しいそうだ。通常何か精神的なストレスを抱えた時、不意に現れたり、相談相手として振る舞ったりする。ごっこ遊びの延長としてのイマジナリーフレンドというのが患者によく見られる症状だと、別の先生からも説明された"),
            who.do("そんなことを言われても実際問題、私のＩＦたちは、きょう子とキョウコは、私にとっての同居人でしかなかった"),
            who.do("自転車を降りて階段を登ろうとしたところで、そこに座り込んでいる見慣れない男性に気づいた"),
            who.do("その彼は隣に座ったきょう子と一緒に、綾取りをして遊んでいる"),
            who.do("え……"),
            who.do("その違和感は、最初は分からなかった"),
            who.talk("あの"),
            who.do("けれどじわじわと足元から這い上がってきて、それが首筋まで到達すると同時に、その正体である彼が私を見て、人懐こい笑顔になった"),
            who.talk("岩根……今日子さん、でいいかな？"),
            who.do("その声は甲高く、少年のそれのように聞こえる"),
            who.talk("そうだけど"),
            who.do("と答えてから思い出した。教室を覗いていたマッシュルームだ"),
            who.talk("おかえり"),
            who.do("十歳の私が言う"),
            who.do("そのきょう子の手の上から指を差し込んで器用に紐を受け取ると、私に向けて真っ直ぐ三本になった川を見せながら、彼も同じようにこう言った"),
            who.talk("おかえり……今日子さん"),
            )


def asuko(w: World):
    who = w.get("who")
    return w.scene("$asuko",
            who.do("その日は椚木先輩が用事があるというので、いつもみたいにファミレスで集まってから解散という流れにはならず、現地でバラバラになった後、幸子と斉藤さんの三人でカフェで一時間ほど過ごした"),
            who.do("実は高校時代に幸子も斉藤さんも男子から告白された経験があると知って驚かされたが、よく考えると私もつい最近、よく分からない男性から同じようなことを言われたのだと思い出す"),
            who.do("アパートのドアを開けて昼下がりの陽が差し込むリビングに戻ると、きょう子もキョウコも横並びで眠っていた。いつもなら騒がしいのに、逆にこんな風だと何かあったんじゃないかと戸惑ったくらいだ"),
            who.do("冷蔵庫の中を確認して妙なものが増えていないかどうかを見る"),
            who.do("あの宮内翔太郎が現れて以来、時々奇妙なことが起こっているから神経質になっていた"),
            who.talk("大丈夫"),
            who.do("わざわざ口に出して安堵すると、部屋に戻り、出されている課題に手をつけようと思ってノートに手を伸ばす"),
            who.do("課題の殆どはレポートで、図書館で借りてきた資料が山積みになっていたが、読むだけでもなかなか骨が折れた"),
            who.do("そういえば斉藤さんが一緒にレポート課題とかやりたいと言っていたことを思い出し、携帯電話を手に取る"),
            who.do("着信記録があった"),
            who.do("それも友だちや大学の知人からではない"),
            who.do("岩根雪雄。私の今の父親だ"),
            who.talk("かけないの、電話？"),
            who.do("え？"),
            who.do("後ろから声がして、でもそれがきょう子のものでもキョウコのものでもなかったから、私は振り返ることができずにそのまま声を返す"),
            who.talk("だれ？"),
            who.talk("誰じゃないでしょう？　こっちを見れば分かる。それとも……また逃げ出す？"),
            who.do("背中を嫌な汗が流れ落ちていった"),
            who.do("心臓は強く早く脈打ち、私は呼吸がうまくできない"),
            who.talk("ま、私のことはいいから、電話してみたら？"),
            who.do("それでも一度だけ、顔を少しだけ回して思い切り目線だけを後ろに飛ばす"),
            who.do("そこには赤い眼鏡を掛けたもう一人の私が、右手を腰にやってじっと立っていた"),
            who.talk("嘘……"),
            who.do("彼女は笑う"),
            who.talk("そんな……そんなはず"),
            who.do("呼吸が苦しい"),
            who.do("視界がちらついて、私は体を開いて後ろを見ると、支えようとした右手から体勢を崩して半分寝たような格好になる"),
            who.do("彼女はそんな私を見下ろしながら近づいてきて、すっと手を伸ばした"),
            who.talk("大丈夫？　岩根今日子さん？"),
            who.talk("あなたは……"),
            who.talk("私はね、岩根明日子《いわねあすこ》。二十歳の学生よ"),
            )


def greeting_asuko(w: World):
    who = w.get("who")
    return w.scene("$asukoの挨拶",
            who.talk("明日子《あすこ》？"),
            who.do("私に手を差し伸べている赤い眼鏡の女性から、逃げ出そうという体勢のままで彼女を見ていた"),
            who.talk("他の今日子たちと何も変わらないのに、何をそんなに怯えているの？"),
            who.do("彼女は私の前で屈《かが》むと、目線の高さを同じにしてチューリップのように重ねた手の上に顎《あご》を置く。革のスカートが膝上まで上がり、すっきりとした脛《すね》が露《あらわ》になる"),
            who.talk("私はもう一人のあなた。だから何も怖がる必要はないの。それともあなたは自分自身が怖いの？　嫌いなの？　目を背《そむ》けたい存在なの？"),
            who.do("喉がカラカラになり、全身の毛穴が開く。嫌な汗が噴き出して、心臓がどんどん早くなる"),
            who.talk("……なんで"),
            who.do("暫《しばら》く見つめ合った後で何とか絞《しぼ》り出せたのが、たったそれだけの言葉だった"),
            who.talk("ＩＦがどうやって生まれるのか、という質問？　それなら三浦先生にでも訊《き》いた方が早いんじゃない？　だって私はあなただもの。あなたの知らないことは私にも分からない"),
            who.talk("ちょっとだけ待って"),
            who.talk("いくらでも待つわよ。時間なんてあってないようなものだし"),
            who.do("私は体を起こして一旦キッチンに引き上げる"),
            who.do("冷蔵庫からペットボトルに入っている今朝作った麦茶を取り出し、コップに注ぎ入れてそれを一気に飲み干す。胸元の気持ち悪い温度が僅《わず》かに下がった気になるが、それでもまだ鼓動は落ち着かないのでもう一杯、麦茶を飲んだ"),
            who.do("部屋を見やると明日子が眠りこけている他の二人を見て微笑している。きょう子の柔らかい髪を撫《な》で、キョウコのお腹にはタオルケットを掛けてやる"),
            who.do("危険はない。自分にそう言い聞かせてみるけれど、頭の中の警戒ランプは消える素振りを見せない"),
            who.do("ただ距離を置いたことで少しずつ落ち着いて考えられるようになり始めた"),
            who.do("岩根明日子と名乗った彼女は、二人の前から動こうとはしない。待ってくれているのか、それとも何か事情があるのか"),
            who.do("三浦先生にはＩＦというのは自分の無意識が作り出したものだから、決して自分自身を傷つけるようなことはしないと教わった。事実、怒鳴ったり喚《わめ》いたりはするけれど、私が彼女たちに傷つけられたということはない。それでも彼女たちを生み出す時は何か強いストレス下にあって、それを緩和する為に彼女たちが必要になるのだと言われた"),
            who.do("ちらり、と肩越しに明日子が私を見る"),
            who.do("彼女は暫くそのまま私を見ていたが、何を思ったのか笑みを見せると、テーブルに置いた携帯電話を手にする。躊躇《ちゅうちょ》なくボタンを押すと、電話のコール音が鳴り響いた"),
            who.talk("何、してるの？"),
            who.do("私は嫌な予感がしてコップとペットボトルを置いて、慌てて部屋に戻る"),
            who.talk("はい。もしもし。今日子さんかな？"),
            who.do("スピーカーから漏れ聞こえたのは、父の声だった"),
            )


def me_and_me(w: World):
    who = w.get("who")
    return w.scene("私は私で",
            who.do("クリニックを出ると、うろこ状になった雲が青い空に綺麗に並んでいた"),
            who.do("人通りの少ない路地を、駅に向かって歩き出す"),
            who.do("スニーカーの足音は自分にだけ響いて、それはたぶん普通のことなのだろうけれど、この一月ばかり、ふとした瞬間に訪れる「わたし」という感覚に戸惑っていた"),
            who.do("きっと誰もが生まれながらにして持っていて、それは「ワタシ」でも「私」でもなく「わたし」なのだけれど、いつからかそれが「私」だったり「僕」だったり或いはもっと他の、その場限りの自分になるのだろう"),
            who.do("わたしがその場専用のワタシになる"),
            who.do("きっとそんな器用さでみんなは迷うこともなく生きている"),
            who.do("でも時々私のような、上手くその場の自分を繕えなくて、どうしていいのか分からないまま、他人と距離を離すことで何とかやりくりしなければいけないような、そんな人もいる"),
            who.do("私にとってきょう子やキョウコの存在は、わたしやワタシを上手く扱えない私という人間を助ける為の、世界からの贈り物だったのかも知れない"),
            who.do("大通りに出ると急に車の音や人の声がよく響いてきて、私は一瞬自分の存在を見失いそうに感じたが、立ち止まり、ゆっくりと空を見上げてから呼吸を整え、今一度視線を戻すと、鼓動も気持ちも落ち着きを取り戻していた"),
            who.do("駅を目指して歩いていく"),
            who.do("すれ違う人、追い抜いていく人、コンビニに入っていく人、タクシーを呼び止めている人、待ち合わせをしているカップル、ベビィカーを押している母親、ハンカチで額を拭うスーツの男性、台車を押して走っていく運送会社の人、そして私の目の前で立ち止まったシャツの少年"),
            who.do("振り返った彼は少しだけ翔太郎に似ている気がしたが、私の脇を素通りしていく"),
            who.do("振り返ると小学生たちの待ち合わせの群れに彼が合流していて、楽しそうな笑い声を上げていた"),
            who.do("私は彼らに背を向けて、歩いていく"),
            who.do("わたしで、"),
            who.do("ワタシで、"),
            who.do("私らしく"),
            )