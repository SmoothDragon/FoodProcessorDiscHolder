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

disc_cut = solid.cylinder(d=outer_d, h=outer_w, center=True)
disc_cut = solid.rotate([0,90,0])(disc_cut)
disc_cut = solid.translate([0,0,outer_d/2])(disc_cut)

drain_hole = solid.cylinder(d=3*outer_w, h=outer_d, center=True)

horiz = core_w*1.1
vert = outer_d*.125
lift = 2

xy_shift = [(0,-vert),(-horiz,vert),(horiz,vert)]
for x,y in xy_shift:
    base -= solid.translate([x,y,lift])(disc_cut)
    base -= solid.translate([x,y,lift])(drain_hole)

final = base
print(solid.scad_render(final, file_header="$fn=64;"))
