#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null
then
 echo "Installing Nginx..."
 sudo apt-get update
 sudo apt-get install -y nginx
fi

# Create necessary directories
echo "Creating directories..."
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create a fake HTML file for testing
echo "Creating test HTML file..."
echo "<html>
 <head>
 </head>
 <body>
  Holberton School
 </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link
echo "Creating symbolic link..."
if [ -h /data/web_static/current ]; then
 sudo rm /data/web_static/current
fi
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user and group
echo "Changing ownership..."
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
echo "Updating Nginx configuration..."
sudo bash -c 'cat << EOF > /etc/nginx/sites-available/default
server {
  listen 80 default_server;
  listen [::]:80 default_server;
  add_header X-Served-By $HOSTNAME;
  root /var/www/html;
  index index.html index.htm;

  location /hbnb_static {
      alias /data/web_static/current;
      index index.html index.htm;
  }

  location /redirect_me {
      return 301 http://cuberule.com/;
  }

  error_page 404 /404.html;
  location /404 {
    root /var/www/html;
    internal;
  }
}
EOF'

# Restart Nginx
echo "Restarting Nginx..."
sudo systemctl restart nginx
