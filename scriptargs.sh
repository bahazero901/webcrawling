#!/bin/bash

if [ $# == 0 ]; then
    echo "You need at least one argument"
else
    echo "Hi $1 $2 $3"
    echo "arg count = $#"
    echo "you args are = $*"
    echo "in a list = $@"
fi
