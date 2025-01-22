#!/usr/bin/env sh

######################################################################
# @author      : Bhishan (Bhishan@BpMacpro.local)
# @file        : run
# @created     : Wednesday Jan 22, 2025 10:07:33 EST
#
# @description : Fun game
######################################################################
#!/bin/bash

# URL to open
URL="http://127.0.0.1:8000"

# Detect the operating system
OS=$(uname)

if [[ "$OS" == "Darwin" ]]; then
    # macOS: Use the 'open' command
    open "$URL"
elif [[ "$OS" == "Linux" ]]; then
    # Linux: Use 'xdg-open' (common for Linux systems)
    xdg-open "$URL"
elif [[ "$OS" =~ ^CYGWIN|MINGW|MSYS ]]; then
    # Windows: Use 'start' command for Google Chrome
    start chrome "$URL"
else
    echo "Unsupported operating system: $OS"
fi

uvicorn app:app --reload



