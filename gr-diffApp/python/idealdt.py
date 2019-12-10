#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2019 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#
import datetime

import numpy as np
from gnuradio import gr, uhd
from numpy.random import random


class idealdt(gr.sync_block):
    """
    docstring for block idealdt
    """
    debug = False

    time_stamp_wave_1 = []
    time_stamp_wave_2 = []

    time_difference = 0.03125  # unit is microsecond
    flag = 3.0

    history_max = 0.0
    deltatime = 0.0

    # frequency must be 1MHz
    delta_time = datetime.timedelta(microseconds=1)

    def __init__(self):
        gr.sync_block.__init__(self,
                               name="idealdt",
                               in_sig=[np.float32, np.float32],
                               out_sig=[np.float32, np.float32])

    def work(self, input_items, output_items):
        # time_now = float(uhd.usrp_sink.get_time_now(self,0))
        # print("time now from usrp")
        # print(time_now)
        # print("output items")
        # print(output_items)
        # print("size of output items")
        # print(len(output_items))

        in0 = input_items[0]
        out0 = output_items[0]
        in1 = input_items[1]
        out1 = output_items[1]
        # <+signal processing here+>

        # print("array")
        # print(input_items[0])
        # print(input_items[1])
        print("size")
        print(len(input_items[0]))
        print(len(input_items[1]))
        print("max")
        print(np.max(input_items[0]))
        print(np.max(input_items[1]))

        max_loc_0 = np.argmax(input_items[0])
        max_loc_1 = np.argmax(input_items[1])

        max_val_0 = np.max(input_items[0])
        max_val_1 = np.max(input_items[1])

        if (self.history_max > 1.00):
            self.history_max = 0.0
        else:
            self.history_max = max(self.history_max, max_val_0, max_val_1)

    
        if (max_val_1 == self.history_max) and (max_val_1 == self.history_max):
            self.deltatime = (max_loc_0 - max_loc_1) * self.time_difference
            if max_loc_0 - max_loc_1 > 0:
                self.flag = 1.0
            else:
                self.flag = 2.0
            print("is computing")
        else:
            print("not computing")
        # print("max loc 0 and 1")
        # print(max_loc_0)
        # print(max_loc_1)
        # print(deltatime)
        # print(max_loc_0 - max_loc_1)

        print("flag")
        print(self.flag)
        print("dt")
        print(self.deltatime)

        print("current time")
        print(datetime.datetime.now())

        if (self.debug):
            self.flag = np.random.randint(1, 100)
            self.deltatime = np.random.randint(1, 4)
        # print("input items")
        # print(input_items)
        # print("size of input items")
        # print(len(input_items))
        # print("input items[0]")
        # print(input_items[0])
        # print("size of input items[0]")
        # print(len(input_items[0]))
        # print("input items[1]")
        # print(input_items[1])
        # print("input items[0][:]")
        # print(input_items[0][:])
        # print("size of output items")
        # print(len(output_items))
        # print("output items")
        # print(output_items)
        # print("finish")

        out0[:] = [self.deltatime]
        out1[:] = [self.flag]
        return len(output_items[0])
