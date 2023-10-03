# This manifest configures a new server with Nginx webser
# and add a custom http response header

package {'nginx':
  ensure   => 'installed',
  provider => 'apt',
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => 'present',
  content => 'Hello World!',
}

file { '/usr/share/nginx/html/custom_404.html':
  ensure  => 'present',
  content => 'Ceci n'est pas une page',
}

$str = "server {
  \tlisten 80 default_server;
  \tlisten [::]:80 default_server;\n
  \troot /var/www/html;\n
  \tindex index.html index.htm index.nginx-debian.html;\n
  \tserver_name nyandi.tech;\n
  \tadd_header X-Served-By \$hostname;\n
  \trewrite ^/redirect_me/$ http://nyandi.tech permanent;\n
  \terror_page 404 /custom_404.html;
  \tlocation = /custom_404.html {
  \t\troot /usr/share/nginx/html;
  \t\tinternal;
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
