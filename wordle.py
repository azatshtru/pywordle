import assembler
from PIL import Image

CATAMARAN = 'Fonts/Catamaran-Black.ttf'
CINZEL = 'Fonts/Cinzel-Regular.ttf'
QUESTRIAL = 'Fonts/Questrial-Regular.ttf'
ZILLA = 'Fonts/ZillaSlab-Bold.ttf'
HEPTA = 'Fonts/HeptaSlab-Bold.ttf'

_file = 'Shrek.txt'
_res = 1024
_des = 100
_varfact = 1
_theme = 'EverythingNice'
_font = HEPTA
_ignore = True

def setwordle(txtfile, res, startsize=100, startvariance=1, theme='EverythingNice', wordfont=HEPTA, ignorance=True):
    global _des
    global _res
    global _file
    global _varfact
    global _theme
    global _font
    global _ignore

    _des = startsize
    _file = txtfile
    _res = res
    _varfact = startvariance
    _theme = theme
    _font = wordfont
    _ignore = ignorance


def wordle():
    global _des
    global _res
    global _file
    global _varfact
    global _theme
    global _font
    global _ignore

    im = assembler.assemble(_file, _res, _res, _font, sizing=_des, variance_factor=_varfact, theme=_theme, condense=True, ignore=_ignore)

    if(im == 'terminate'):
        print("Time taken too long, checking again with reduced sizes.")
        _des /= 2
        wordle()

    if(im != None and im != 'terminate' and type(im) != 'str'):
        im.show()
        im.save("wordle.png")