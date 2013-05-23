#!/bin/sh

#get build info by PID
function buildinfo() {
    EPPIC_PID=$1;
    EPPIC_HOME=`ls -ld /proc/$EPPIC_PID/cwd | awk '{print $NF}'`
    BUILD_INFO_FILE=$EPPIC_HOME/config/com/tps/config/com_tps_sysmgmt_BuildInfo_properties
    if [ -f $BUILD_INFO_FILE ]; then
        BUILD_INFO=`head -n 1 $BUILD_INFO_FILE | awk '{print $1}'`
    fi
    if [ -z $BUILD_INFO ]; then
        BUILD_INFO="UNKNOWN BUILD"
    fi
    echo $BUILD_INFO
}

#get ip address
function ipaddress() {
    /sbin/ifconfig eth0 | awk '/inet addr/ {print $2}' | awk -F: '{print $2}'
}

#get avalable port
function unusedport() {
    BPORT=0
    for i in `seq 2020 65535`; do
        TEMPPORT=`netstat -atn|grep -w $i|awk '{print $4}'`
        TEMPPORT2=${TEMPPORT##*:}
        if [ -z $TEMPPORT2 ]; then
            BPORT=$i
            break
        fi
    done
    echo $BPORT
}

