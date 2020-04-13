#!/bin/sh
function cleanup() {
    sudo killall python3
}

trap cleanup SIGINT

python3 ./src/api.py & 
python3 ./src/sensor.py
