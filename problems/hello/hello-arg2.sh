#!/bin/bash

if [[ $# -ne 2 ]]; then
    echo Usage: $0 You need two arguments
    exit 1
fi

echo "$1, $2!"
