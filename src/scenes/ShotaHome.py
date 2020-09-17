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
    who = w.get("who")
    r            who.do("松本に聞いた宮内翔太郎の実家は、私が彼から聞かされた印象のままの真っ白な二階建てだった"),
            who.do("大きな木造の塀に囲まれていて、格子状になった開き戸と車用だろう、大きなシャッターが降ろされた門があり、私は恐る恐る『宮内』とだけ書かれた表札の下のインタフォンを押した"),
            who.do("一分ほどだろうか。応答があって男性の声がすると、私はたどたどしさをどうにもできないまま、何とか翔太郎の知り合いで、彼が亡くなったことを知ってやってきたことを告げた"),
            who.talk("分かりました。ちょっと待ってて下さい"),
            who.do("そう言われて緊張が取れないまま待っていると、ほどなくして戸が開けられた。現れたのは髪が真っ白になった彼の父親らしき男性だった"),
            who.talk("さあ、どうぞ"),
            who.talk("突然すみません。お邪魔します"),
            who.do("その男性の優しく目元が緩むと、やはり翔太郎の面影を感じさせた"),
            who.do("私は彼について中に入る。五十メートルほどの前庭があり、植木や花で玄関に向かう石畳以外は鬱蒼《うっそう》としていた"),
eturn w.scene('$ln_shota家',
            )

