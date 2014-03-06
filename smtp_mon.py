#!/usr/bin/env python

import os
import rrdtool
import simple_smtp

def cpu_rrd():
    if not os.path.exists("CPU.rrd"):
        rrdtool.create('CPU.rrd',
                'DS:Data_Source_Name:GAUGE:600:U:U',
                'RRA:AVERAGE:0.5:1:120')
    else:
        rrdtool.update('CPU.rrd', 'N:%s' % simple_smtp.snmp_cpuload())

def cpu_graph():
    pass

if __name__ == '__main__':
    cpu_rrd()
