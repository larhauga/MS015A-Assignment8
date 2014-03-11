#!/usr/bin/env python

import os, sys
import rrdtool
import simple_snmp
import time

def cpu_rrd():
    filename = "CPU.rrd"
    database_name = "CPU_Usage"
    heartbeat = 60 # The time available for input
    if not os.path.exists(filename):
        rrdtool.create(filename,
		'--start', 
		'now',
		'--step',
		'60', # How often the data is collected
                'DS:%s:GAUGE:%d:U:U' % (database_name, heartbeat),
                'RRA:AVERAGE:0.5:1:120')

    ret = rrdtool.update(filename, '%d:%s' % (int(time.time()),
            str(simple_snmp.snmp_cpuload())))
    print "Added entry, Time: %d, CPU: %s" % (int(time.time()),
            str(simple_snmp.snmp_cpuload()))

    if ret:
        print rrdtool.error()

def cpu_graph():
    ret = rrdtool.graph( "net.png", 
	"--start", 
	"-1h", 
	"--vertical-label=CPU Load",
        "DEF:CPU_Usage=CPU.rrd:CPU_Usage:AVERAGE",
        "AREA:CPU_Usage#00FF00:CPU",
        "GPRINT:CPU_Usage:AVERAGE:CPU\: %6.2lf\\r")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        cpu_rrd()
    elif sys.argv[1] == "graph":
        cpu_graph()

