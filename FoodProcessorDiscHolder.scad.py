#!/usr/bin/env python3

'''
Make a holder for food processor blades
'''

import solid
import math


outer_d = 155
outer_w = 2.5
core_d = 29.5
core_w = 14

base = solid.sphere([outer_d, 3*core_d, core_d])

final = base
print(solid.scad_render(final, file_header="$fn=256;"))
