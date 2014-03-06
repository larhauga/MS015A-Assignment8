#!/usr/bin/env python

from pysnmp.entity.rfc3413.oneliner import cmdgen

def snmp_get(host):
    community = 'public'

    cmdg = cmdgen.CommandGenerator()
    commdata = cmdgen.CommunityData('username','public')
    transport = cmdgen.UdpTransportTarget((host, 161))
    variables = (1,3,6,1,2,1,1,1,0)
    err_ind, err_status, err_index, result = cmdg.getCmd(commdata, transport,
            variables)
    print err_ind
    print err_index
    print err_status
    print result


if __name__ == '__main__':
    print snmp_get("localhost")
