# SPDX-FileCopyrightText: Copyright (c) 2023 Tim C
#
# SPDX-License-Identifier: MIT
"""

"""

import board
import displayio
from displayio_json_inflater.absolute_layout import AbsoluteLayout

f = open("layouts/simpletest.json", "r")
layout_str = f.read()
f.close()
main_layout = AbsoluteLayout(board.DISPLAY, layout_str)

board.DISPLAY.show(main_layout.view)

# main_layout.sub_view_by_index(0).label.text = "Changed Text\nBy Index"
main_layout.sub_view_by_id("main_lbl").label.text = "Changed\nText By Id"

while True:
    pass
