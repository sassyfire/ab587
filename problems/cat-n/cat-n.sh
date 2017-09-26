#!/bin/bash

if [[ $# -eq 0 ]]; then
    printf "Usage: %s file\n" "$(basename "$0")"
    exit 1
fi

FILE=$1
i=0
while read -r LINE; do
    let i++
    echo "\"$i: $LINE\""
done < "$FILE"


