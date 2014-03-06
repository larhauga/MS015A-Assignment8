#!/usr/bin/env python

import os
import rrdtool
import simple_smtp

def cpu_rrd():
    if not os.path.exists("CPU.rrd"):
        rrdtool.create('CPU.rrd',
                'DS:cpu_load:GAUGE:600:U:U',
                'RRA:AVERAGE:0.5:1:120')
        rrdtool.update('CPU.rrd', 'cpu_load N:%s' % simple_smtp.snmp_cpuload())
    else:
        rrdtool.update('CPU.rrd', 'cpu_load N:%s' % simple_smtp.snmp_cpuload())


def cpu_graph():
    pass

if __name__ == '__main__':
    if len(sys.argv) == 1:
        cpu_rrd()
    elif sys.argv[1] == "graph":
        cpu_graph()

