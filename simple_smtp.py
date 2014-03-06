#!/usr/bin/env python

from pysnmp.entity.rfc3413.oneliner import cmdgen

def snmp_get(host, variables):
    community = 'public'

    cmdg = cmdgen.CommandGenerator()
    commdata = cmdgen.CommunityData('username','public')
    transport = cmdgen.UdpTransportTarget((host, 161))
    err_ind, err_status, err_index, result = cmdg.getCmd(commdata, transport,
            variables)

    if err_ind:
        print(err_ind)
        return None
    else:
        if err_status:
            print('%s at %s' % (err_status.prettyPrint(),
                            error_ind and result[int(errorIndex)-1]) or '?')
            return None
        else:
            return result

def snmp_cpuload():
    result = snmp_get("localhost", (1,3,6,1,4,1,2021,10,1,3,1))
    if result:
        return float(result[0][1])
    else:
        return float(-1)

def snmp_all(host):
    cpu1min = (1,3,6,1,4,1,2021,10,1,3,1)
    cpu5min = (1,3,6,1,4,1,2021,10,1,3,2)
    cpu15min= (1,3,6,1,4,1,2021,10,1,3,3)
    hostname= (1,3,6,1,2,1,1,1,0)

    print snmp_get(host, hostname)
    print snmp_get(host, cpu1min)
    print snmp_get(host, cpu5min)
    print snmp_get(host, cpu15min)
    print snmp_cpuload()

if __name__ == '__main__':
    snmp_cpuload()
