from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.live import Live

import time
import os
import random

from introscreen import *

#$$$$$$$$$$#

def reset_confeti_layer_and_color_matrix() -> None :
    global CONFETI_LAYER
    global CONFETTI_COLOR_MATRIX
    for _ in range(int(len(GRAPHICS_MATRIX)*len(GRAPHICS_MATRIX[0])*random.randint(1, 100)/100)) :
        try :
            if CONFETI_FILLED_INDEX != [] :
                index = CONFETI_FILLED_INDEX.pop(0)
                CONFETI_LAYER[index[0]][index[1]] = " "
            else : break
        except : pass

def live_renderer() -> Panel :
    global CONFETI_FILLED_INDEX
    text = ""

    reset_confeti_layer_and_color_matrix()

    for _ in range(int(len(GRAPHICS_MATRIX)*len(GRAPHICS_MATRIX[0])*(random.randint(0, 6)/100))) :
        row = random.randint(0, len(GRAPHICS_MATRIX)-1)
        col = random.randint(0, len(GRAPHICS_MATRIX[0])-1)
        if GRAPHICS_MATRIX[row][col] == " " :
            if col > 0 and GRAPHICS_MATRIX[row][col-1] != "\\" :
                CONFETI_LAYER[row][col] = random.choice(CONFETI_CHARACTERS)
                CONFETTI_COLOR_MATRIX[row][col] = random.choice(CONFETI_COLORS)
                CONFETI_FILLED_INDEX.append([row, col])
            elif col == 0 :
                CONFETI_LAYER[row][col] = random.choice(CONFETI_CHARACTERS)
                CONFETTI_COLOR_MATRIX[row][col] = random.choice(CONFETI_COLORS)
                CONFETI_FILLED_INDEX.append([row, col])

    for _ in range(len(GRAPHICS_MATRIX)) :
        for __ in range(len(GRAPHICS_MATRIX[0])) :
            if GRAPHICS_MATRIX[_][__] != " " :
                text += GRAPHICS_MATRIX[_][__]
            else :
                if CONFETI_LAYER[_][__] != " " :
                    text += "[{0}]{1}[/{0}]".format(CONFETTI_COLOR_MATRIX[_][__],
                                                    CONFETI_LAYER[_][__])
                    pass
                else :
                    text += " "
        if _ != len(GRAPHICS_MATRIX)-1 :
            text += "\n"
    return Panel(text,
                 expand=True)

def animator() -> None :
    with Live(live_renderer(), refresh_per_second=20) as L :
        while True :
            time.sleep(0.1)
            L.update(live_renderer())

#$$$$$$$$$$#
if __name__ == "__main__" :
    animator()
