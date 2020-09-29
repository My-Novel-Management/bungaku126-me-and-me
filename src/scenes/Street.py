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
    kyo = w.get("kyoko")
    return w.scene('家路・街の明かり',
            # NOTE: omitしたのでここの要素を他で入れる
            w.cmd.change_stage("Street"),
            kyo.do("自転車で路地を駆け抜ける"),
            kyo.do("段差で少し跳ねて、前の籠に入れた買い物袋の中の生卵のことが気になったけれど、この前のように落とした訳じゃないから大丈夫だろうと思うことにした"),
            kyo.do("見上げた空は雲が多くて、それでも最近はこの時間もまだまだ明るい。路地の街灯はぼんやりとした光を放ち始め、帰宅途中の学生や会社員をそれとなく照らしている"),
            kyo.do("この辺りは学生が暮らすアパートが多いけれど、明かりの付いた住宅から漂ってくるのは家庭の夕食の香りだった"),
            kyo.do("子供たちのはしゃぐ声に、母親の声が重なる"),
            kyo.do("ちょっと苛立ったやり取りのようだったけれど、それでもどこかごく普通の家庭のそれに思えて、私は腰を上げペダルを漕ぐ足に力を入れた"),
            kyo.do("ここ最近は暑い日が続いていたが、このくらいの時間帯になればしっとりと空気が落ち着いて、幾分心地良い。風を切って走るこの時間が、私を色々なものから自由にしてくれるような気がして、好きだった"),
            )


def goto_univ(w: World):
    kyo = w.get("kyoko")
    return w.scene("大学に向かう",
            w.cmd.change_stage("Street"),
            kyo.be(),
            kyo.do("アパートの駐輪場から地面を蹴って漕ぎ出すとバスを待つ賑やかな小学生の声が響いてきた",
                "黄色いカバーを付けたランドセルを見ると自分の低学年の頃を思い出すと$full_sachiが言っていたけれど、",
                "$Sのその頃の記憶はとてもおぼろげだ",
                "皆無とは言わないけれど担任がどんな顔をしていて男性だったか女性だったかすら思い出せない"),
            kyo.do("丁字路を右に曲がりしばらく行くと大通りが待っている",
                "北海道の道は随分と広くて真っ直ぐだと他の地域から来た学生に教えてもらったがずっとそれで暮らしていると当たり前が過ぎて、",
                "常に車が列を成して渋滞しているという彼女たちのぼやきがよく分からない"),
            kyo.do("心置きなくペダルを回して広々とした歩道を駆け抜ける", "&"),
            kyo.do("大学までの十分程度のこの道のりが$Mの心をほんの少しだけ解き放ってくれる大切なひと時だった"),
            kyo.do("けれど空を見上げると雲がしっかりと蓋をして、今にも、と思っていたら地面に小さなシミが湧き上がるように付いて、一気に雨が降り始めた"),
            )


def meet_mushroom(w: World):
    kyo = w.get("kyoko")
    sk = w.get("sjkyoko")
    sho = w.get("shota")
    return w.scene("マッシュルームに出会う",
            w.cmd.change_stage("Street"),
            kyo.be(),
            kyo.do("仕事を終えて外に出た時には、すっかり夜の街に様変わりしていた",
                "客引きがネクタイを緩めて歩くスーツの男性の一群に必死に声を掛け、",
                "バニーのコスプレをした女性がティッシュを配っては愛想を振りまいている",
                "横断歩道を挟んだ向こう側では酔っぱらいらしい男性がカップルに大声を振り上げ、それを周囲の人が離れて傍観していた"),
            kyo.do("私も将来、あの中の誰かになるのだろうか"),
            kyo.do("そんなことを考えながら横断歩道を渡ると地下鉄の駅へと急いだ"),
            kyo.do("十分ほどで大学前まで戻ると、駐輪場に自転車を取りに行ってから夜道を帰る",
                "午前中に降っていた雨は小さな水たまりを道の縁に作っていてタイヤが思い切り跳ね飛ばしてしまった",
                "あいにくと誰にも迷惑を掛けることはなかったが少しだけスニーカーが濡れてしまったのが心地悪い"),
            kyo.do("夜風を受けながらペダルを漕ぐのも悪くはないのだけれどこういった不慮の出来事に襲われやすいので、",
                "どうしても心も体も早くアパートに戻りたがっている",
                "それでも途中スーパーに立ち寄り見切り品の一つでも仕入れて帰らないと冷蔵庫の中には卵と牛乳とキャベツの切れ端に三分の一の人参があるだけだ"),
            kyo.do("膨らんだ買い物袋を前籠に放り込み、あまり外灯の多くない路地を進む",
                "三分ほどで薬局の看板が見え、その電信柱を左に曲がるとアパートの前の外灯が明滅しているのが確認できた",
                "それは$Mの胃袋を少しだけ重くさせる"),
            kyo.do("普通ＩＦ、つまりイマジナリーフレンドを持つというのはその人物にとっての精神安定剤のようなものらしいが、",
                "三浦先生にも指摘されたように$Mのように常にアパートにいて一緒に暮らしている他人のように振る舞うというのは珍しいそうだ",
                "通常何か精神的なストレスを抱えた時に不意に現れたり相談相手として振る舞ったりする",
                "ごっこ遊びの延長としてのイマジナリーフレンドというのが患者によく見られる症状だと別の先生からも説明された"),
            kyo.do("けれど$Mにとっての彼女たちは現実だ",
                "少なくともＩＦの、$sjkyokoと$jrkyokoは同居人でしかなかった"),
            kyo.do("自転車をアパートの駐輪場に停め、階段を登ろうとしたところでそこに座り込んでいる見慣れない男性の姿に気づいた", "&"),
            sk.be(),
            sho.be(),
            kyo.do("しかもその男性は隣に座った$sjkyokoと一緒に綾取りをして遊んでいる"),
            kyo.do("その違和感は最初は分からなかった"),
            kyo.talk("あの"),
            kyo.do("けれどじわじわと足元から這い上がってきてそれが首筋まで到達すると$Mは息が喉元で留まり、眉根がきゅっと寄ったのと同時に彼は人懐こい笑顔になって尋ねた"),
            sho.talk("大丈夫？　$kyokoさん"),
            kyo.do("その声は甲高く少年のそれのように聞こえる"),
            kyo.talk("そうだけど"),
            kyo.do("薄暗い中それでもよく目立つレモンイエローのパーカーと七部丈のパンツ、足元はバスケットシューズのように見える",
                "何より栗毛色をしたマッシュルーム頭はすぐに$Mの今日の記憶の中から彼のことを引っ張り出してきた",
                "朝講堂で見たあの男子生徒だ"),
            sk.talk("おかえり"),
            kyo.do("十歳の私が言う"),
            kyo.do("そのきょう子の手の上から指を差し込んで器用に紐を受け取ると、私に向けて真っ直ぐ三本になった川を見せながら彼も同じようにこう言った"),
            sho.talk("おかえり……今日子さん"),
            )


def asuko(w: World):
    kyo = w.get("kyoko")
    asu = w.get("asuko")
    return w.scene("$asuko",
            w.cmd.change_stage("Street"),
            kyo.be(),
            kyo.do("その日は椚木先輩が用事があるというのでいつもみたいにファミレスで集まってから解散という流れにはならず現地でバラバラになった後、",
                "幸子と斉藤さんの三人でカフェで一時間ほど過ごした"),
            kyo.do("実は高校時代に幸子も斉藤さんも男子から告白された経験があると知って驚かされたが、よく考えると私もつい最近よく分からない男性から同じようなことを言われたのだと思い出す"),
            kyo.do("アパートのドアを開けて昼下がりの陽が差し込むリビングに戻ると、きょう子もキョウコも横並びで眠っていた",
                "いつもなら騒がしいのに、逆にこんな風だと何かあったんじゃないかと戸惑ったくらいだ", "&"),
            kyo.do("冷蔵庫の中を確認して妙なものが増えていないかどうかを見る", "&"),
            kyo.do("あの宮内翔太郎が現れて以来、時々奇妙なことが起こっているから神経質になっていた"),
            kyo.talk("大丈夫"),
            kyo.do("わざわざ口に出して安堵すると部屋に戻り、出されている課題に手をつけようと思ってノートに手を伸ばす", "&"),
            kyo.do("課題の殆どはレポートで図書館で借りてきた資料が山積みになっていたが読むだけでもなかなか骨が折れた", "&"),
            kyo.do("そういえば斉藤さんが一緒にレポート課題とかやりたいと言っていたことを思い出し、携帯電話を手に取る"),
            kyo.do("着信記録があった", "&"),
            kyo.do("それも友だちや大学の知人からではない", "&"),
            kyo.do("岩根雪雄。私の今の父親だ"),
            asu.be(),
            asu.talk("かけないの、電話？"),
            kyo.do("え？"),
            kyo.do("後ろから声がして、でもそれがきょう子のものでもキョウコのものでもなかったから私は振り返ることができずにそのまま声を返す"),
            kyo.talk("だれ？"),
            asu.talk("誰じゃないでしょう？　こっちを見れば分かる。それとも……また逃げ出す？"),
            kyo.do("背中を嫌な汗が流れ落ちていった", "&"),
            kyo.do("心臓は強く早く脈打ち、私は呼吸がうまくできない"),
            asu.talk("ま、私のことはいいから、電話してみたら？"),
            kyo.do("それでも一度だけ、顔を少しだけ回して思い切り目線だけを後ろに飛ばす"),
            kyo.do("そこには赤い眼鏡を掛けたもう一人の私が、右手を腰にやってじっと立っていた"),
            kyo.talk("嘘……"),
            kyo.do("彼女は笑う"),
            kyo.talk("そんな……そんなはず"),
            kyo.do("呼吸が苦しい"),
            kyo.do("視界がちらついて、私は体を開いて後ろを見ると、支えようとした右手から体勢を崩して半分寝たような格好になる", "&"),
            kyo.do("彼女はそんな私を見下ろしながら近づいてきて、すっと手を伸ばした"),
            asu.talk("大丈夫？　岩根今日子さん？"),
            kyo.talk("あなたは……"),
            asu.talk("私はね、岩根明日子。二十歳の学生よ"),
            )


def greeting_asuko(w: World):
    kyo = w.get("kyoko")
    asu = w.get("asuko")
    yukio = w.get("yukio")
    return w.scene("$asukoの挨拶",
            w.cmd.change_stage("Street"),
            kyo.be(),
            asu.be(),
            kyo.talk("明日子？"),
            kyo.do("$Mに手を差し伸べている赤い眼鏡の女性から逃げ出そうという体勢のままで、彼女を見ていた", "&"),
            asu.talk("他の今日子たちと何も変わらないのに、何をそんなに怯えているの？"),
            kyo.do("彼女は私の前で屈むと目線の高さを同じにしてチューリップのように重ねた手の上に顎を置く",
                "革のスカートが膝上まで上がり、すっきりとした脛が露になった"),
            asu.talk("私はもう一人のあなた。だから何も怖がる必要はないの。それともあなたは自分自身が怖いの？　嫌いなの？　目を背けたい存在なの？"),
            kyo.do("喉がカラカラになり、全身の毛穴が開く",
                "嫌な汗が噴き出して、心臓がどんどん早くなる"),
            kyo.talk("……なんで"),
            kyo.do("暫く見つめ合った後で何とか絞り出せたのが、たったそれだけの言葉だった"),
            asu.talk("ＩＦがどうやって生まれるのか、という質問？　それなら三浦先生にでも訊いた方が早いんじゃない？　だって私はあなただもの。あなたの知らないことは私にも分からない"),
            kyo.talk("ちょっとだけ待って"),
            asu.talk("いくらでも待つわよ。時間なんてあってないようなものだし"),
            kyo.do("私は体を起こして一旦キッチンに引き上げる", "&"),
            kyo.do("冷蔵庫からペットボトルに入っている今朝作った麦茶を取り出し、コップに注ぎ入れてそれを一気に飲み干す",
                "胸元の気持ち悪い温度が僅かに下がった気になるがそれでもまだ鼓動は落ち着かないのでもう一杯、麦茶を飲んだ"),
            kyo.do("部屋を見やると明日子が眠りこけている他の二人を見て微笑している",
                "きょう子の柔らかい髪を撫で、キョウコのお腹にはタオルケットを掛けてやる"),
            kyo.do("危険はない。自分にそう言い聞かせてみるけれど頭の中の警戒ランプは消える素振りを見せない"),
            kyo.do("ただ距離を置いたことで少しずつ落ち着いて考えられるようになり始めた"),
            kyo.do("岩根明日子と名乗った彼女は二人の前から動こうとはしない",
                "待ってくれているのか、それとも何か事情があるのか", "&"),
            kyo.do("三浦先生にはＩＦというのは自分の無意識が作り出したものだから決して自分自身を傷つけるようなことはしないと教わった",
                "事実、怒鳴ったり喚いたりはするけれど、私が彼女たちに傷つけられたということはない",
                "それでも彼女たちを生み出す時は何か強いストレス下にあってそれを緩和する為に彼女たちが必要になるのだと言われた"),
            kyo.do("ちらり、と肩越しに明日子が私を見る"),
            kyo.do("彼女は暫くそのまま私を見ていたが何を思ったのか笑みを見せると、テーブルに置いた携帯電話を手にする",
                "躊躇なくボタンを押すと電話のコール音が鳴り響いた"),
            kyo.talk("何、してるの？"),
            kyo.do("私は嫌な予感がしてコップとペットボトルを置いて慌てて部屋に戻る"),
            yukio.talk("はい。もしもし。今日子さんかな？"),
            kyo.do("スピーカーから漏れ聞こえたのは、父の声だった"),
            )


def me_and_me(w: World):
    kyo = w.get("kyoko")
    return w.scene("私は私で",
            w.cmd.change_stage("Street"),
            kyo.be(),
            kyo.do("クリニックを出るとうろこ状になった雲が青い空に綺麗に並んでいた"),
            kyo.do("人通りの少ない路地を駅に向かって歩き出す"),
            kyo.do("スニーカーの足音は自分にだけ響いてそれはたぶん普通のことなのだろうけれど、",
                "この一月ばかり、ふとした瞬間に訪れる「わたし」という感覚に戸惑っていた", "&"),
            kyo.do("きっと誰もが生まれながらにして持っていて、それは「ワタシ」でも「私」でもなく「わたし」なのだけれど、",
                "いつからかそれが「私」だったり「僕」だったり或いはもっと他の、その場限りの自分になるのだろう"),
            kyo.do("わたしがその場専用のワタシになる"),
            kyo.do("きっとそんな器用さでみんなは迷うこともなく生きている"),
            kyo.do("でも時々私のような、上手くその場の自分を繕えなくて、",
                "どうしていいのか分からないまま他人と距離を離すことで何とかやりくりしなければいけないような、そんな人もいる", "&"),
            kyo.do("私にとってきょう子やキョウコの存在はわたしやワタシを上手く扱えない私という人間を助ける為の、世界からの贈り物だったのかも知れない"),
            kyo.do("大通りに出ると急に車の音や人の声がよく響いてきて私は一瞬自分の存在を見失いそうに感じたが、",
                "立ち止まり、ゆっくりと空を見上げてから呼吸を整え、今一度視線を戻すと、鼓動も気持ちも落ち着きを取り戻していた"),
            kyo.do("駅を目指して歩いていく"),
            kyo.do("すれ違う人、追い抜いていく人、コンビニに入っていく人、タクシーを呼び止めている人、待ち合わせをしているカップル、",
                "ベビィカーを押している母親、ハンカチで額を拭うスーツの男性、台車を押して走っていく運送会社の人、そして私の目の前で立ち止まったシャツの少年", "&"),
            kyo.do("振り返った彼は少しだけ翔太郎に似ている気がしたが私の脇を素通りしていく"),
            kyo.do("振り返ると小学生たちの待ち合わせの群れに彼が合流していて、楽しそうな笑い声を上げていた"),
            kyo.do("私は彼らに背を向けて、歩いていく"),
            kyo.do("わたしで、"),
            kyo.do("ワタシで、"),
            kyo.do("私らしく"),
            )
