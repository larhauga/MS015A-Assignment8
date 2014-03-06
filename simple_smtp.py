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
            for name, val in result:
                print("%s: %s" % (name.prettyPrint(), val.prettyPrint()))
            return result

if __name__ == '__main__':
    host    = "localhost"
    cpu1min = (1,3,6,1,4,1,2021,10,1,3,1)
    cpu5min = (1,3,6,1,4,1,2021,10,1,3,2)
    cpu15min= (1,3,6,1,4,1,2021,10,1,3,3)
    hostname= (1,3,6,1,2,1,1,1,0)

    print snmp_get(host, hostname)
    print snmp_get(host)
