# -*- coding: utf-8 -*-
'''
Story Config
============
'''

ASSET = {
        "PERSONS": (
            # (tag / name / full / age (birth) / job / call / info)
            ("kyoko", "今日子", "岩根,今日子", 20,(1,1), "female", "大学生", "me:私:dad:雪雄さん"),
            ("jrkyoko", "キョウコ", "", 15,(1,1), "female", "中学生", "me:ワタシ"),
            ("sjkyoko", "きょう子", "", 10,(1,1), "female", "小学生", "me:わたし"),
            ("asuko", "明日子", "岩根,明日子", 20,(1,1), "female", "大学生", "me:私"),
            ("mother", "朝子", "岩根,朝子", 48,(1,1), "female", "介護職員"),
            ("yukio", "雪雄", "岩根,雪雄", 45,(1,1), "male", "営業"),
            ("shota", "翔太郎", "宮内,翔太郎", 20,(1,1), "male", "謎の男", "me:ボク"),
            ("yoshi", "芳雄", "宮内,芳雄", 50,(1,1), "male", "翔太郎の父", "me:僕"),
            ("sachi", "幸子", "砂山,幸子", 20,(1,1), "female", "大学生", "me:あたし"),
            ('matsu', '松本', '', 20,(1,1), 'male', '大学生', "me:俺"),
            ("asumi", "亜純", "", 20,(1,1), "female", "バイト", "me:あたし"),
            ("kunugi", "椚木", "", 22,(1,1), "female", "大学生"),
            ("saito", "斉藤", "", 21,(1,1), "female", "大学生", "me:わたし"),
            ("oshi", "押谷", "", 52,(1,1), "male", "大学助教授"),
            ("isoya", "磯谷", "", 50,(1,1), "male", "大学教授（ドイツ語）"),
            ("miura", "三浦", "", 45,(1,1), "male", "心療内科医", "me:私"),
            ("suzu", "鈴森", "鈴森,実里", 33,(1,1), "female", "会社員"),
            ("arase", "荒瀬", "荒瀬,省二", 40,(1,1), "male", "会社員"),
            ),
        "STAGES": (
            # (tag / name / parent / (geometry) / info)
            ("Sapporo", "札幌市", "Japan"),
            ("HokkaidoUniv", "北海大学", "Sapporo"),
            ("UnivCampus", "大学キャンパス", "HokkaidoUniv"),
            ("Classroom", "教室", "HokkaidoUniv"),
            ("LectureHall", "講堂", "HokkaidoUniv"),
            ("Library", "大学図書館", "HokkaidoUniv"),
            ("RamenShop", "ラーメン屋", "Sapporo"),
            ("MaruyamaPark", "円山公園", "Sapporo"),
            ("Station", "駅", "Sapporo"),
            ("SapporoStation", "札幌駅", "Sapporo"),
            ("Street", "路地", "Sapporo"),
            ("Apart", "アパート", "Sapporo"),
            ("KyokoRoom", "二〇四号室", "Apart"),
            ("DataInc", "（株）アクセルリンク", "Sapporo"),
            ("SoupCurry", "スープ湯珈利", "Sapporo"),
            ("Famires", "ファミレス", "Sapporo"),
            ("AroundStation", "駅前通り", "Sapporo"),
            ("Hotel", "ラブホテル", "Sapporo"),
            ("ShotaHome", "宮内家", "Sapporo"),
            ("ShotaHomeDrawing", "応接間", "ShotaroHome"),
            ("ShotaRoom", "翔太郎の部屋", "ShotaroHome"),
            ("InTrain", "電車内", "Sapporo"),
            ("Clinic", "三浦クリニック", "Sapporo"),
            ("OnBycycle", "自転車", "Sapporo"),
            ("BycycleParking", "大学の駐輪場", "HokkaidoUniv"),
            ("MatsuApart", "松本のアパート", "Sapporo"),
            ),
        "DAYS": (
            # (tag / name / month / day / year)
            ("ShotaBirthday", "翔太郎の誕生日", 6, 4, 2000),
            ("DepartDay", "離婚した日", 6,4, 2005),
            ("ShotaDeadDay", "翔太郎が亡くなった日", 8,10, 2010),
            ("MeetShota", "翔太郎に会った日", 6,4, 2020),
            ("VisitMiyauchi", "宮内家訪問", 8,10, 2020),
            ("VisitClinic", "診察日", 9,10, 2020),
            ),
        "TIMES": (
            # (tag / name / hour / minute)
            ),
        "ITEMS": (
            # (tag / name / cate / info)
            ),
        "WORDS": (
            # (tag / name / cate / info)
            ),
        "RUBIS": (
            # (origin / rubi / exclusions / always)
            ),
        }

