#!/bin/bash

if [[ $# -eq 0 ]]; then
    printf "Usage: %s [NUM] FILE\n" "$(basename "$0")" 
    exit 1
fi 

FILE=$1
NUM=${2:-3}
i=-1

if [[ ! -f $FILE ]]; then
        echo "$FILE is not a file"
        exit 1
fi

while read -r LINE; do
    let i++
    if [[ $i -eq $NUM ]]; then 
    break
    fi
        echo "$LINE"
    done < $FILE

