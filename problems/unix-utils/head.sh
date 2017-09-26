#!/bin/bash

if [[ $# -eq 0 ]]; then
    printf "Usage: %s FILE\n" "$(basename "$0")" 
    exit 1
fi

FILE=$1
i=$2
while read -r LINE; do
    let i++
    echo "$LINE"
done < $FILE






