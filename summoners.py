import pyautogui
import time

screen = pyautogui.screenshot()

TOTAL_MONSTERS = 39

TK_NORMAL = (1100, 420)
TK_HARD = (1250, 420)
TK_NIGHTMARE = (1450, 420)
RC_NORMAL = (1100, 620)
RC_HARD = (1250, 620)
RC_NIGHTMARE = (1450, 620)
JR_NORMAL = (1100, 820)
JR_HARD = (1250, 820)
JR_NIGHTMARE = (1450, 820)

ALL_MAPS = [
    TK_NORMAL,
    TK_HARD,
    TK_NIGHTMARE,
    RC_NORMAL,
    RC_HARD,
    JR_NORMAL,
    JR_HARD
]

MONSTER_POSITIONS = [
    (1150, 270), (1270, 270), (1385, 270),
    (1150, 445), (1270, 445), (1385, 445),
    (1150, 620), (1270, 620), (1385, 620),
]

STANDARD_LOADOUT = [
    15, 26, 16,
    27, 37, 22,
    32, 33, 24
]

ICE_LOADOUT = [
    15, 32, 16,
    17, 10, 19,
    22, 33, 26
]

FIRE_LOADOUT = [
    15, 26, 16,
    23, 25, 22,
    32, 33, 24
]

LIGHTNING_LOADOUT = [
    15, 26, 16,
    23, 25, 22,
    32, 33, 24
]

ICE = ((1138, 336), LIGHTNING_LOADOUT)
FIRE = ((1135, 633), ICE_LOADOUT)
LILIGHTNING = ((1089, 906), FIRE_LOADOUT)


def screenshot():
    global screen
    screen = pyautogui.screenshot()


def defaultClick(pos):
    pyautogui.click(pos[0], pos[1])
    time.sleep(0.2)


def isPixelThisColor(xy, rgb):
    return screen.getpixel(xy) == rgb


def selectMap(nextMap, fixLoadout, loadout):
    defaultClick(nextMap)
    time.sleep(1.2)
    if fixLoadout:
        selectLoadout(loadout)
    defaultClick((1266, 993))


def getAchievments():
    if isPixelThisColor((1491, 132), (24, 207, 244)):
        defaultClick((1473, 120))
        defaultClick((1415, 211))

        # verificando se é outro além do primeiro
        screenshot()
        if not isPixelThisColor((1414, 363), (156, 62, 36)):
            defaultClick((1414, 363))
        if not isPixelThisColor((1411, 486), (156, 62, 36)):
            defaultClick((1411, 486))
        if not isPixelThisColor((1456, 609), (156, 62, 36)):
            defaultClick((1456, 609))
        if not isPixelThisColor((1453, 741), (156, 62, 36)):
            defaultClick((1453, 741))
        if not isPixelThisColor((1455, 862), (156, 62, 36)):
            defaultClick((1455, 862))

        defaultClick((1501, 99))
        screenshot()


def rollMonsters():
    if isPixelThisColor((1061, 183), (24, 207, 244)):
        defaultClick((1020, 202))
        defaultClick((1087, 991))
        defaultClick((1036, 148))
        defaultClick((1275, 740))
        defaultClick((1507, 71))


def rollMythic():
    mythic = False
    while True:
        defaultClick((1520, 115))
        pyautogui.moveTo(1227, 670)
        pyautogui.drag(0, -500, 0.3)
        time.sleep(0.4)
        defaultClick((1109, 529))
        defaultClick((1500, 249))

        defaultClick((1012, 202))
        defaultClick((1456, 986))
        defaultClick((1046, 150))

        # Preciso descobrir a cor
        screenshot()
        if (not isPixelThisColor((1165, 174), (208, 88, 30))
                and not isPixelThisColor((1170, 179), (138, 29, 162))):
            mythic = True

        defaultClick((1313, 723))
        defaultClick((1506, 90))

        if mythic:
            defaultClick((1266, 784))
            defaultClick((1164, 729))
            defaultClick((1274, 594))

        defaultClick((1519, 121))
        pyautogui.moveTo(1227, 670)
        pyautogui.drag(0, -100, 0.3)
        time.sleep(0.4)
        defaultClick((1076, 520))
        time.sleep(0.2)
        defaultClick((1271, 748))

        while True:
            time.sleep(0.1)
            screenshot()

            if isPixelThisColor((1343, 639), (165, 238, 66)):
                defaultClick((1288, 625))
                if mythic:
                    defaultClick((1288, 625))
                else:
                    defaultClick((1277, 411))
                defaultClick((1146, 766))
                break

        if mythic:
            defaultClick((234, 19))
            pyautogui.moveTo((1414, 558))
            pyautogui.drag(-400, 0, 0.4)
            time.sleep(0.2)
            defaultClick((1431, 279))
            time.sleep(5)
            break

        while True:
            time.sleep(0.1)
            screenshot()

            if isPixelThisColor((1525, 214), (204, 22, 50)):
                time.sleep(0.5)
                defaultClick((1511, 221))
                break

        if mythic:
            break


def passMonitor():
    if isPixelThisColor((1230, 585), (239, 43, 53)):
        # verifica se não é anuncio
        screenshot()
        if not isPixelThisColor((1304, 584), (255, 255, 255)):
            defaultClick((1304, 584))
            time.sleep(0.2)
            defaultClick((1304, 584))
        else:
            defaultClick((1230, 585))


def passAction(x, y, delta, timer):
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown()
    pyautogui.move(0, delta, timer)
    time.sleep(0.4)
    pyautogui.mouseUp()


def passMonster(times):
    i = 0
    while i < times:
        if times - i >= 6:
            passAction(1050, 970, -915, 0.301)
            i += 6
        elif times - i >= 5:
            passAction(1050, 860, -795, 0.3)
            i += 5
        elif times - i >= 4:
            passAction(1050, 750, -632, 0.3)
            pyautogui.mouseUp()
            i += 4
        elif times - i >= 3:
            passAction(1050, 610, -475, 0.3)
            pyautogui.mouseUp()
            i += 3
        elif times - i >= 2:
            passAction(1050, 490, -335, 0.2)
            pyautogui.mouseUp()
            i += 2
        else:
            passAction(1050, 370, -170, 0.2)
            i += 1


def selectLoadout(loadout):
    for pos in range(9):
        defaultClick((MONSTER_POSITIONS[pos][0],
                      MONSTER_POSITIONS[pos][1] + 80))
        defaultClick(MONSTER_POSITIONS[pos])

        monster = loadout[pos]
        delta = max(monster - (TOTAL_MONSTERS - 5), 0)
        passMonster(min(monster, (TOTAL_MONSTERS - 5)))
        defaultClick((1128, 240 + delta * 130))
        defaultClick((1513, 1004))


def normalWave(nextMap, fixLoadout):
    selectMap(nextMap, fixLoadout, STANDARD_LOADOUT)

    i = 0
    while i < 100:
        time.sleep(0.1)
        screenshot()

        getAchievments()
        rollMonsters()
        passMonitor()

        # perdendo fase
        if isPixelThisColor((1266, 798), (20, 9, 6)):
            time.sleep(2)
            defaultClick((1133, 784))
            defaultClick((1148, 722))
            break

        # ganhando fase
        if isPixelThisColor((1246, 607), (29, 76, 71)):
            defaultClick((1259, 798))
            break

        # Fail Safety
        i += 1
        if i == 90:
            defaultClick((1497, 96))
            defaultClick((1263, 585))
            i = 0


def farmBlueCoin():
    # Selecionando fase
    defaultClick((1391, 146))
    defaultClick((1389, 483))

    # Verirfica se precisa gastar gemas
    screenshot()
    if isPixelThisColor((1350, 550), (252, 161, 255)):
        defaultClick((1350, 550))
        defaultClick((1389, 483))

    # Refaz o loadout
    time.sleep(1.5)
    selectLoadout(STANDARD_LOADOUT)
    defaultClick((1256, 993))

    i = 0
    while i < 100:
        time.sleep(0.1)
        screenshot()

        getAchievments()
        rollMonsters()

        # verifica automatico
        if isPixelThisColor((1030, 780), (161, 60, 31)):
            defaultClick((1030, 780))

        # verificando caso derrota
        if isPixelThisColor((1243, 605), (65, 42, 26)):
            time.sleep(2)
            defaultClick((1143, 785))
            break

        # verificando caso vitoria
        if isPixelThisColor((1260, 597), (29, 78, 73)):
            time.sleep(2)
            defaultClick((1401, 825))
            break

        # Fail Safety
        i += 1
        if i == 90:
            defaultClick((1497, 96))
            defaultClick((1263, 585))
            i = 0


def farmGem(element, fixLoadout):
    # Selecionando fase
    defaultClick((1391, 146))
    pyautogui.moveTo(1253, 910)
    pyautogui.drag(0, -500, 0.4)
    time.sleep(0.4)
    defaultClick(element[0])

    # Verirfica se precisa gastar gemas
    screenshot()
    if isPixelThisColor((1350, 550), (252, 161, 255)):
        defaultClick((1350, 550))
        defaultClick(element[0])

    time.sleep(1)
    # Arrumando loadout
    if(fixLoadout):
        time.sleep(0)
        selectLoadout(element[1])
    defaultClick((1229, 1009))

    i = 0
    while i < 100:
        time.sleep(0.1)
        screenshot()
        getAchievments()
        rollMonsters()
        passMonitor()

        # perdendo fase
        if isPixelThisColor((1266, 798), (20, 9, 6)):
            time.sleep(2)
            defaultClick(((1138, 772)))
            break

        # Fail Safety
        i += 1
        if i == 90:
            defaultClick((1497, 96))
            defaultClick((1263, 585))
            i = 0


def farmAds():
    selectMap(TK_NORMAL, False, False)

    i = 0
    while i < 100:
        time.sleep(0.1)
        screenshot()

        if isPixelThisColor((1230, 585), (239, 43, 53)):
            screenshot()
            if isPixelThisColor((1304, 584), (255, 255, 255)):
                time.sleep(1)
                defaultClick((1304, 584))
                time.sleep(40)
                defaultClick((1510, 60))
                defaultClick((1510, 60))
                defaultClick((1007, 59))
                defaultClick((1007, 59))
                time.sleep(1)
                defaultClick((1269, 592))
                defaultClick((1438, 72))
                break

        getAchievments()
        rollMonsters()
        passMonitor()

        # Fail Safety
        i += 1
        if i == 90:
            defaultClick((1497, 96))
            defaultClick((1263, 585))
            i = 0


def main():
    # selectLoadout(STANDARD_LOADOUT)

    # for nextMap in ALL_MAPS:
    #     normalWave(nextMap, False)

    for i in range(1):
        print("Mythics: " + str(i+1))
        rollMythic()

    # for i in range(6):
    #     print("Ad: " + str(i+1))
    #     farmAds()

    # for i in range(500):
    #     print("Gem: " + str(i+1))
    #     farmGem(FIRE, False)

    # for i in range(500):
    #     print("Blue Coin: " + str(i+1))
    #     farmBlueCoin()

    # for i in range(5000):
    #     print("Normal Run: " + str(i+1))
    #     normalWave(JR_HARD, False)


if __name__ == "__main__":
    main()
