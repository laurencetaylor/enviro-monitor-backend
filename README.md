# Enviroplus Sensor Backend [WIP]

## How to Run

Required hardware:
- Raspberry Pi
- Enviro+ environment sensor
- PMS5003 particulate matter sensor

These instructions are to be run on your Raspberry Pi provided the above hardware is configured correctly

1. Clone this repository
2. Install dependencies with `pip install -r requirements.txt`
3. Install the enviroplus library by running `./install.sh`
4. We will use pm2 to run our app. Install it globally with `npm i -g pm2` (ensure you have node downloaded first)
5. Start the api and sensor with `pm2 start src/api.py` and `pm2 start src/sensor.py`
6. Run `pm2 startup systemd` then run the generated command followed by `pm2 save`. This will start the app on every raspberry pi boot
7. We will use nginx as a reverse proxy. Install it by running `sudo apt update` followed by `sudo apt install nginx`
8. Replace the contents of /etc/nginx/sites-available with the following code:
````
server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;

	index index.html index.htm index.nginx-debian.html;

	server_name _;

	location / {
		proxy_pass http://localhost:5000;
		proxy_http_version 1.1;
		proxy_set_header Upgrade $http_upgrade;
		proxy_set_header Connection 'upgrade';
		proxy_set_header Host $host;
		proxy_cache_bypass $http_upgrade;
	}
}
````
8. Start nginx with `sudo systemctl start nginx`, or if it already running `sudo systemctl restart nginx`
9. Find out your Raspberry Pi's url with `arp -a` (do not run this on your pi), visit the `/readings` endpoint to view your data