#!/bin/zsh

# Clear the screen for a clean presentation
clear

echo "=========================================="
echo "        MAC CORE SHELL REPORT             "
echo "=========================================="

# 1. Look up the current active Mac username
echo "👤 CURRENT USER:  $(whoami)"

# 2. Get the current calendar date and formatting
echo "📅 CURRENT DATE:  $(date '+%A, %B %d, %Y')"

# 3. Pull the name of the Wi-Fi network your Mac is connected to
# (This uses a built-in Mac network tool called wdutil)
# Fallback block that detects if Apple redacted the Wi-Fi name
RAW_NAME=$(ipconfig getsummary en0 | awk -F ' SSID : ' '/ SSID : / {print $2}')
if [[ "$RAW_NAME" == "<redacted>" || -z "$RAW_NAME" ]]; then
    WIFI_NAME="Protected (macOS Privacy Layer)"
else
    WIFI_NAME="$RAW_NAME"
fi
echo "🌐 WI-FI NETWORK: $WIFI_NAME"

echo "=========================================="


