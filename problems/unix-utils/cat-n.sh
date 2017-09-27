#!/bin/bash

FILE=$1
i=0

if [[ $# -eq 0 ]]; then
   printf "Usage: %s file\n" "$(basename "$0")"
   exit 1

else

if [[ ! -f $FILE ]]; then
   echo "$FILE is not a file"
   exit 1
fi
fi

while read -r LINE; do
   let i++
   echo "$i $LINE"
   done < $FILE


