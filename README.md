# Enviroplus Sensor Backend

A very simple app which continuously collects and exposes [Enviro](https://shop.pimoroni.com/products/enviro?variant=31155658457171) and [PMS5003](https://shop.pimoroni.com/products/pms5003-particulate-matter-sensor-with-cable) data from the moment you boot your Raspberry Pi.

[Initial Setup](https://github.com/LaurenceTaylor/enviro-monitor-backend#initial-setup) | [API Schema](https://github.com/LaurenceTaylor/enviro-monitor-backend#api-schema) | [Todo](https://github.com/LaurenceTaylor/enviro-monitor-backend#todo)

Note: I am not a Python developer 🙂

## Initial Setup

Required hardware:
- Raspberry Pi
- Enviro+ environment sensor
- PMS5003 particulate matter sensor

These instructions are to be run on your Raspberry Pi provided the above hardware is configured correctly.

Readings are taken every 10 minutes by default, determined by the argument for the `run` function in `src/sensor.py`.

1. Clone this repository
2. Install dependencies with `pip install -r requirements.txt`
3. Install the enviroplus library by running `./install.sh`
4. We will use pm2 to run our app. After install Node, install it globally with `npm i -g pm2` 
5. Start the api and sensor with `pm2 start src/api.py` and `pm2 start src/sensor.py`
6. Run `pm2 startup systemd` followed by the generated command and `pm2 save`. This will start your app on every raspberry pi boot
7. We will use nginx as a reverse proxy. Install it with `sudo apt update` followed by `sudo apt install nginx`
8. Replace the contents of `/etc/nginx/sites-available` with the following code:
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
8. Start nginx with `sudo systemctl start nginx`, or if already running `sudo systemctl restart nginx`
9. Visit your Raspberry Pi's IP address at the `/readings` endpoint to view your data. Set a `limit` query string to pull a certain number of readings from the database. To find your devices IP address you could use `arp -a` or similar

## API Schema

### GET /readings
Returns all readings. An optional querystring can be passed containing any or all of `dateFrom`, `dateTo`, and `limit` parameters.

#### Example query
`/readings?dateFrom=2020-04-16&dateTo=2020-04-20&limit=100`

#### Example Response
Responses follow the [JSON:API](https://jsonapi.org/) spec.
View the [Pimoroni docs](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-enviro-plus) to learn more about what these readings mean.

````
[
  {
    "id": 154,
    "type": "readings",
    "data": {
      "attributes": {
        "date": "2020-04-16 21:25:11",
        "pressure": 639.2067642784692,
        "temperature": 21.44291390865692,
        "pm25": 6,
        "humidity": 56.04009747852809
      }
    }
  }
]
````

## Todo

- Add tests
