#!/bin/bash

#awk '/.*.apple.com/ { print $5 } /80/ {print $6}' testfile


if [ $# -eq 0 ]; then
    echo "Please enter the file you would like to scan. When you run the script"
    exit 1
fi

awk '/.*.apple.com/ { printf("%s%s\t",$5,$6) }
/80/ {
if ($6 == "")
	print "Apache not installed";
else
	printf("Server is running %s version %s \n",$4,$6)
}' $1