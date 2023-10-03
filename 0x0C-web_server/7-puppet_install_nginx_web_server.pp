# This manifest configures a new server with Nginx webser

package {'nginx':
  ensure   => 'installed',
  provider => 'apt',
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => 'present',
  content => 'Hello World!',
}

$str = "server {
  \tlisten 80 default_server;
  \tlisten [::]:80 default_server;\n
  \troot /var/www/html;\n
  \tindex index.html index.htm index.nginx-debian.html;\n
  \tserver_name nyandi.tech;\n
  \trewrite ^/redirect_me/$ http://nyandi.tech permanent;\n
  \tlocation / {
  \t\ttry_files \$uri \$uri/ =404;
  \t}
}"

file {'/etc/nginx/sites-available/default':
  ensure  => 'present',
  backup  => '.bak',
  content => $str,
}

service {'nginx':
  ensure => 'running',
  enable => 'true',
  restart => 'service nginx restart',
}
