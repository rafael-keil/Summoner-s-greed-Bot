import pyautogui
import time

TK_NORMAL = (2073, 415)
TK_HARD = (2268, 415)
TK_NIGHTMARE = (2415, 415)
RC_NORMAL = (2073, 625)
RC_HARD = (2268, 625)
RC_NIGHTMARE = (2415, 625)
JR_NORMAL = (2073, 835)
JR_HARD = (2268, 835)
JR_NIGHTMARE = (2415, 835)


def defaultClick(x, y):
    pyautogui.click(x, y)
    time.sleep(0.2)


def selectMap():
    pyautogui.click(JR_HARD)
    time.sleep(1.5)
    defaultClick(2260, 990)


def main():

    i = 0
    while i < 10:
        time.sleep(0.2)
        screenshot = pyautogui.screenshot()

        def isPixelThisColor(xy, rgb):
            return screenshot.getpixel(xy) == rgb

        # pegar recompensas
        if isPixelThisColor((2470, 134), (24, 207, 244)):
            defaultClick(2453, 116)
            defaultClick(2459, 213)

            # verificando se é o segundo ou terceiro
            achScreenshot = pyautogui.screenshot()
            if achScreenshot.getpixel((2451, 360)) != (156, 62, 36):
                defaultClick(2451, 360)
            if achScreenshot.getpixel((2448, 486)) != (156, 62, 36):
                defaultClick(2448, 486)

            defaultClick(2478, 104)

        # rodar montros
        if isPixelThisColor((2042, 182), (24, 207, 244)):
            defaultClick(1999, 206)
            defaultClick(2064, 985)
            defaultClick(2021, 152)
            defaultClick(2248, 728)
            defaultClick(2482, 75)

        # fechar anuncio
        if isPixelThisColor((2129, 614), (231, 38, 53)):
            # verifica se não é anuncio
            sellScreenshot = pyautogui.screenshot()
            if sellScreenshot.getpixel((2299, 585)) == (246, 252, 254):
                defaultClick(2129, 614)
            else:
                defaultClick(2344, 578)
                defaultClick(2344, 578)

        # reiniciar fase
        if isPixelThisColor((2239, 779), (20, 9, 6)):
            time.sleep(2)
            defaultClick(2112, 792)
            defaultClick(2116, 704)
            selectMap()

        if isPixelThisColor((2018, 566), (23, 55, 53)):
            defaultClick(2248, 807)
            selectMap()


if __name__ == "__main__":
    main()
