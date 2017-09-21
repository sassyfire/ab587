#!/bin/bash

if [[ $# -ne 1 ]]; then
    echo Usage: $0 YOU ARE WRONG. THE NUMBER OF ARGUMENTS DOES NOT EQUAL TO 1
    exit 1
fi

echo "Hello, $1!"
