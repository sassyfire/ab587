#!/bin/bash

if [[ $# -eq 0 ]]; then
   printf "Usage: %s file\n" "$(basename "$0")"
   exit 1
fi

FILE=$1
i=0

if [[ -f $FILE ]]; then
   while read -r LINE; do
   let i++
   echo "$i $LINE"
   done < $FILE
else
   echo "\"$FILE\" is not a file"
   exit 1
fi

