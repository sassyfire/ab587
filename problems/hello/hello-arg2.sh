#!/bin/bash

if [[ $# -ne 2 ]]; then
    echo Usage: $0 greeting name
    exit 1
fi

echo "$1, $2!"
