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
def shotaro_and_mother(w: World):
    kyo = w.get("kyoko")
    sho = w.get("shota")
    return w.scene('$shotaと母親の話',
            w.cmd.change_stage("Famires"),
            w.cmd.change_time("evening"),
            kyo.be(),
            sho.be(),
            kyo.do("五分後、$meは$shotaと人のごった返しているファーストフード店で適当に注文を済ませて二階の窓際の一画で二人して横並びに座っていた"),
            sho.talk("それで、きょう子ちゃんちゃんたちはまだ見つからないの？"),
            kyo.do("彼はハンバーガーの包み紙を全部引っぺがしてしまってから躊躇なく大口でかぶりつく"),
            kyo.talk("うん"),
            kyo.do("力なく答えると私はストローを咥えてオレンジジュースを啜った"),
            kyo.do("席は入れ替わり立ち替わりにお客さんがやってきては空いた場所を埋めるように収まって談笑を開始する",
                "一人で来ている客も多かったが大半が誰か友人知人と訪れているみたいだ"),
            kyo.do("そういえばこういう場所に男性と二人で来るの初めてかも知れない、と気づいて途端に私は頬が熱くなる",
                "もっとちゃんと化粧をして出てくれば良かった"),
            sho.talk("もしあの子たちが本当にそのＩＦだとすれば、消えたってことはもう必要なくなったからなんじゃないの？"),
            kyo.do("出会った頃から変わらない耳までを隠すマッシュルームカットの茶髪が、冷房の風に靡く",
                "口の端にソースを付けたままそのくりっとした瞳で私の心を覗き込むようにした彼は、考え込んだまま何も言おうとしない私のポテトを一本引き抜いて食べた"),
            kyo.talk("そういうことすると、怒られたんだ"),
            sho.talk("あ、ごめん。悪気はなかったんだ"),
            kyo.do("そうじゃないの、と首を横に振り私は続ける"),
            kyo.talk("私の母親はね、手順とか決まりとかにうるさい人だったの",
                "いつもご飯は大皿に入っていて取り分けるんじゃなくて、個人個人が小鉢なんかに盛られて、好き嫌いせずに全部を綺麗に食べることを強要された。だから大好きな玉子焼きとかウインナーは決まった数以上には食べさせてもらえなかった"),
            kyo.do("一人暮らしになって一番自由になったのは食べ物に関する全てだった",
                "食べ方、食べる順序、量、箸の持ち方からナイフとフォークの使い方まで",
                "何故そこまでを母である彼女が拘ったのか今でも私には分からない",
                "それでもその拘りは彼女を追い詰めるほどに彼女自身にとって必要なものだったのだろう"),
            kyo.do("そう。私にきょう子たちが必要だったように"),
            sho.talk("色々な家庭があるんだね。ボクは食べることだけでなく色々な面でかなり自由にさせてくれたよ",
                "でも何でもしていい、好きなものだけ食べていいっていうのは、本当に自分のことを考えてのことなんだろうかなって、この頃になって疑問に思うようになってさ"),
            kyo.do("彼は長い睫毛を瞳に被せてその視線を私から顔も知らない、けれど同じ空気を吸っている大勢へと向ける"),
            kyo.talk("私にはその気持ちはよく分からないけど、愛しているから何でもさせてやりたいというのは、何も親子に限った話じゃないと思う"),
            sho.talk("じゃあ今日子もボクを愛していたら、何でもさせてくれるの？"),
            kyo.do("突然食いつくように私を見つめたから慌てて椅子から立ち上がってしまう"),
            sho.talk("そのさ……まだ、結婚の約束のこと、思い出してくれてないんだよね？"),
            kyo.talk("ごめんなさい。私、記憶が曖昧な時期があって"),
            kyo.do("彼が顔を逸したことに安堵して、椅子に座り直す",
                "それでも少し距離を置いたままにしたのはいつの間にか彼への警戒心が薄れていたことに気づいたからだ"),
            kyo.talk("今でも五歳前後とか、小学校の頃の教室の様子とか、訊かれてもうまく思い出せないの。記憶喪失とは違ってただ思い出せないだけ。ひょっとしたらその頃の私は生きてなかったんじゃないのかなって思ってる"),
            sho.talk("生きて、ない？"),
            kyo.talk("ええ"),
            kyo.do("小さな噛み跡の付いたバンズの間からソースが紙を伝ってトレイに落ちた", "&"),
            kyo.do("どうしてか彼の目は私ではなくその落ちたソースを見つめていて、何度か「生きてない」と寂しそうに呟く"),
            kyo.talk("実際に生きてなかった訳じゃなくて、その、比喩表現というか、実感としてそうだったのかなって思うだけです"),
            sho.talk("今日子はさ"),
            kyo.do("その彼の手が、オレンジジュースを取ろうとした私の手を押さえる"),
            sho.talk("誰にも心を開かないまま生きていこうとしているの？"),
            kyo.do("彼の指の形が分かるくらい、私の手にその熱が伝わった"),
            kyo.do("その所為だろうか。心臓が少しだけいつもと違う風に跳ねた気がした"),
            )


def senpai_talk(w: World):
    kyo = w.get("kyoko")
    sachi, matsu, saito = w.get("sachi"), w.get("matsu"), w.get("saito")
    kunugi = w.get("kunugi")
    return w.scene("先輩の話",
            w.cmd.change_stage("Famires"),
            w.cmd.change_time("afternoon"),
            kyo.come(),
            sachi.be(),
            kunugi.be(),
            matsu.be(),
            saito.be(),
            kyo.do("じっとりと汗を掻きながらファミレスに入る"),
            sachi.talk("今日子、こっち！"),
            kyo.do("既に奥の四人席には幸子と斉藤さんが座っていて$Mは店員に断ってそっちに歩いていく",
                "入り口を振り返ると松本と椚木先輩が何やら話しながら入ってきたところだった"),
            saito.talk("久しぶり"),
            kyo.do("そう言って斉藤さんはわざわざ自分の隣を開けて私を誘導する",
                "一瞬迷ったけれど他にも続けて入ってくる先輩たちの姿を見て仕方なく奥から詰めて座ることにした"),
            sachi.talk("斉藤さんが最近返事ないからって気にしてたんだけどさ、今日子ひょっとして実家に帰ったりしてたの？"),
            kyo.talk("ううん。バイトが忙しかっただけ"),
            kyo.do("幸子は少しだけ事情を知っている",
                "私と母親の仲が良くないことや友だち付き合いが得意ではないことなんかを"),
            kyo.do("ほんとに？　という彼女の視線に微笑を返してから、私は手を挙げて現れた椚木先輩に頭を下げる"),
            kunugi.talk("これ教室でミーティングしてたら軽く逝ける温度だね。文明の利器さまさまだ"),
            kyo.do("先輩たちも珍しく全員揃い、四人席を三つも占拠して店内に賑やかな一画を作ってしまう",
                "それでも他のサークルほど騒ぐ人もいないので演劇部も掛け持ちしている椚木先輩の声が大きいのが少し迷惑な程度だった"),
            kyo.do("全員の注文が揃うとささやかな乾杯の音頭と共に椚木先輩のハッピーバースディが歌われる",
                "誕生日そのものは一週間ほど前なのだが全員揃うのが今日しかなかった為だ"),
            kunugi.talk("みんな、ありがとう。プレゼントはまた個別に受け付けることにして、明後日の清掃ボランティアなんだけど、それを最後に私はしばらくサークルに顔出さないことにしたから"),
            kyo.talk("何でですか？"),
            kyo.do("きっと誰もがそう感じただろうに声を上げたのは私だけだった"),
            kunugi.talk("岩根、ありがとうね。将来のことも考えて、ちょっと本気で演劇に打ち込もうと思って。九月にある劇団のオーディション、受かりたい"),
            kyo.do("先輩たちはみんな知っていたのか黙ってそれを聞いている", "&"),
            kyo.do("斉藤さんは当然として幸子も私も勿論聞いてなくて松本を見ると考え込んだ様子で先輩と私を見ていた"),
            kunugi.talk("そういう事情もあって、部の今後のことを、二年たち中心に話し合ってもらいたいなって思ってる。どうだろうか"),
            kyo.do("四年生たちの視線は幸子や松本ではなく私に集まり、斉藤さんがいつの間にか私の右腕をぎゅっと掴んでいた", "&"),
            kyo.do("私はすぐには答えられず代わりに幸子が、"),
            sachi.talk("わたしたちで考えておきます"),
            kyo.do("珍しく真剣な顔で答えた"),
            kyo.do("椚木先輩の「じゃあ食べよっか」の声で場の空気は元に戻ったように見えたが、私の心の中は波立ったまま落ち着く様子もなく、",
                "目の前にしたチキンドリアは熱くて、なんでこんなもの頼んでしまったのだろうという後悔を抱えたままいつまでもスプーンを口には運べないでいた"),
            matsu.talk("なあ"),
            kyo.do("ミーティングが解散になったところで松本から声を掛けられた"),
            kyo.do("私の頭はすっかりこの後幸子と斉藤さんの三人で今後の話をすることに向いていたのに彼の重苦しい声に「何？」と振り向かずにはいられなかった"),
            matsu.talk("ちょっと、訊きたいことがあってさ"),
            kyo.do("そう言って彼が見せてくれたのはまだ小さい頃の翔太郎が写った写真だった",
                "画像ではなく、つるんとした照り返しのある写真",
                "少し古いものみたいで端の白いところが一部黄色くなっていた"),
            kyo.talk("えっと……"),
            kyo.do("見た瞬間に心は決まっていたけれど言葉を上手く選べずに視線を前にいた幸子と斉藤さんに向ける"),
            sachi.talk("あ、じゃあわたしは斉藤ちゃんと二人でデートしとくから、今日子は松本とデートしなよ"),
            kyo.do("冗談のつもりなんだろうけれど突然デートなんて言われて斉藤さんは慌てていた",
                "けれど幸子は強引に彼女の腕を取ると、そのまま連れて行ってしまう"),
            saito.talk("岩根さんあとでちゃんと連絡するから！"),
            kyo.do("その姿は連行されていく容疑者みたいな有様だったけれど、私は手を振って見送ると改めて松本に向き直る"),
            matsu.talk("その写真のこと、教えて欲しい"),
            )
