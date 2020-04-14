# Enviroplus Sensor Backend [WIP]

## How to Run

- Clone this repository
- Install requirements with `pip install -r requirements.txt`
- Install the enviroplus library by running `./install.sh`
- Install pm2 globally `npm i -g pm2`
- Start the api and sensor with `pm2 start src/api.py`, `pm2 start src/sensor.py`
- Install nginx, create file /etc/nginx/sites-available
- Paste the following code in
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
- Start nginx with `sudo systemctl start nginx`
- Find out raspberry pi url with `arp -a`, given correct configuration visit the `<url>/readings` endpoint for data