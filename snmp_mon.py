#!/usr/bin/env python

import os, sys
import rrdtool
import simple_snmp
import time

def cpu_rrd():
    filename = "CPU.rrd"
    database_name = "CPU_Usage"
    heartbeat = 60
    if not os.path.exists(filename):
        rrdtool.create(filename,
                '--step',
                heartbeat,
                'DS:%s:GAUGE:%d:U:U' % (database_name, heartbeat),
                'RRA:AVERAGE:0.5:1:120')

    ret = rrdtool.update(filename, '%d:%f' % (int(time.time()),
            str(simple_snmp.snmp_cpuload())))
    print "Added entry, Time: %d, CPU: %f" % (int(time.time()),
            str(simple_snmp.snmp_cpuload()))
    if ret:
        print rrdtool.error()

def cpu_graph():
    ret = rrdtool.graph( "net.png", "--start", "-1d", "--vertical-label=CPU Load",
        "DEF:inoctets=test1.rrd:input:AVERAGE",
        "DEF:outoctets=test1.rrd:output:AVERAGE",
        "AREA:inoctets#00FF00:In traffic",
        "LINE1:outoctets#0000FF:Out traffic\\r",
        "CDEF:inbits=inoctets,8,*",
        "CDEF:outbits=outoctets,8,*",
        "COMMENT:\\n",
        "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf %Sbps",
        "COMMENT:  ",
        "GPRINT:inbits:MAX:Max In traffic\: %6.2lf %Sbps\\r",
        "GPRINT:outbits:AVERAGE:Avg Out traffic\: %6.2lf %Sbps",
        "COMMENT: ",
        "GPRINT:outbits:MAX:Max Out traffic\: %6.2lf %Sbps\\r")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        cpu_rrd()
    elif sys.argv[1] == "graph":
        cpu_graph()

