#!/usr/bin/env python3

'''
Make a holder for food processor blades
'''

import solid
import math

inf = 1000

upper_half_space = solid.cube(2*inf, center=True)
upper_half_space = solid.translate([0,0,inf])(upper_half_space)

outer_d = 155
outer_w = 2.5
core_d = 29.5
core_w = 14

base = solid.sphere(d=1)
base = solid.scale([3*core_d, outer_d, core_d])(base)
base = solid.intersection()(base, upper_half_space)

final = base
print(solid.scad_render(final, file_header="$fn=256;"))
