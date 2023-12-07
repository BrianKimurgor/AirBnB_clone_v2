# Install Nginx
package { 'nginx':
 ensure => installed,
}

# Create necessary directories
file { '/data/web_static/releases/test/':
 ensure => directory,
 owner => 'ubuntu',
 group => 'ubuntu',
 mode  => '0755',
}

file { '/data/web_static/shared/':
 ensure => directory,
 owner => 'ubuntu',
 group => 'ubuntu',
 mode  => '0755',
}

# Create a fake HTML file for testing
file { '/data/web_static/releases/test/index.html':
 ensure => file,
 owner  => 'ubuntu',
 group  => 'ubuntu',
 mode   => '0644',
 content => '<html>
               <head>
               </head>
               <body>
                Holberton School
               </body>
             </html>',
}

# Create symbolic link
file { '/data/web_static/current':
 ensure => link,
 target => '/data/web_static/releases/test/',
 owner => 'ubuntu',
 group => 'ubuntu',
}

# Update Nginx configuration
file { '/etc/nginx/sites-available/default':
 ensure => file,
 owner  => 'root',
 group  => 'root',
 mode   => '0644',
 content => template('nginx/default.conf.erb'),
}

# Restart Nginx
service { 'nginx':
 ensure => running,
 enable => true,
}
