#!/usr/bin/env python

from pysnmp.entity.rfc3413.oneliner import cmdgen

def snmp_get(host):
    community = 'public'
    #cg = cmdgen.CommandGenerator()
    #comm_data = cmdgen.CommunityData('','public')

    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData(community),
        cmdgen.UdpTransportTarget((host, 161)),
        cmdgen.MibVariable('SNMPv2-MIB', 'sysName', 0)
    )

    # Check for errors and print out results
    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex)-1] or '?'
                )
            )
        else:
            for name, val in varBinds:
                print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))

if __name__ == '__name__':
    print snmp_get("localhost")
