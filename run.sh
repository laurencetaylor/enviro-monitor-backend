#!/bin/sh
echo "Running enviroplus script..."
function cleanup() {
    sudo killall python3
}

trap cleanup SIGINT

python3 ./src/api.py & 
# Frequent bug in library where script fails 'pms5003.ReadTimeoutError: PMS5003 Read Timeout' the first time it is run
python3 ./src/sensor.py
python3 ./src/sensor.py
