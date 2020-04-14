# Enviroplus Sensor Backend [WIP]

## How to Run

- Clone this repository
- Install requirements with `pip install -r requirements.txt`
- Install the enviroplus library by running `./install.sh`
- Install pm2 globally `npm i -g pm2`
- Start the api and sensor with `pm2 start src/api.py`, `pm2 start src/sensor.py`
- Start nginx with `sudo systemctl start nginx`
- Find out raspberry pi url with `arp -a`, given correct configuration visit the `<url>/readings` endpoint for data