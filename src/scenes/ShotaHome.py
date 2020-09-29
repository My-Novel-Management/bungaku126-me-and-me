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
def miyauchi_home(w: World):
    kyo = w.get("kyoko")
    yoshi = w.get("yoshi")
    return w.scene("$ln_shota家",
            w.cmd.change_stage("ShotaHome"),
            w.cmd.change_time("midmorning"),
            kyo.come(),
            kyo.do("松本に聞いた宮内翔太郎の実家は私が彼から聞かされた印象のままの真っ白な二階建てだった"),
            kyo.do("大きな木造の塀に囲まれていて格子状になった開き戸と車用だろう、大きなシャッターが降ろされた門があり、",
                "私は恐る恐る『宮内』とだけ書かれた表札の下のインタフォンを押した", "&"),
            kyo.do("一分ほどだろうか",
                "応答があって男性の声がすると私はたどたどしさをどうにもできないまま、何とか翔太郎の知り合いで彼が亡くなったことを知ってやってきたことを告げた"),
            yoshi.be(),
            yoshi.talk("分かりました。ちょっと待ってて下さい"),
            kyo.do("そう言われて緊張が取れないまま待っていると、ほどなくして戸が開けられた",
                "現れたのは髪が真っ白になった彼の父親らしき男性だった"),
            yoshi.talk("さあ、どうぞ"),
            kyo.talk("突然すみません。お邪魔します"),
            kyo.do("その男性の優しく目元が緩むとやはり翔太郎の面影を感じさせた"),
            kyo.do("私は彼について中に入る。五十メートルほどの前庭があり、植木や花で玄関に向かう石畳以外は鬱蒼としていた"),
            )
