# This manifest configure a new server with Nginx
# and creates a custom header X-Served-By HOSTNAME

package {'nginx':
  ensure   => 'installed',
  provider => 'apt',
}

exec {'ufw':
  command => 'ufw allow \'Nginx HTTP\'',
  path    => '/usr/sbin/',
}

$str = "server {
  \tlisten 80 default_server;
  \tlisten [::]:80 default_server;\n
  \troot /var/www/html;\n
  \tindex index.html index.htm index.nginx-debian.html;\n
  \tserver_name nyandi.tech;\n
  \tadd_header X-Served-By \$hostname;\n
  \trewrite ^/redirect_me/$ http://nyandi.tech permanent;\n
  \tlocation = /custom_404.html {
  \t\troot /usr/share/nginx/html;
  \t\tinternal;"
  \t}
}"

file {'/etc/nginx/sites-available/default':
  ensure  => 'present',
  backup  => '.bak',
  content => $str,
}

file {'/usr/share/nginx/html/custom_404.html':
  ensure  => 'present',
  content => 'Ceci n'est pas une page',
}

service {'nginx':
  ensure  => 'running',
  enable  => 'true',
  restart => 'service nginx restart',
}
