# This manifest configure a new server with Nginx
# and creates a custom header X-Served-By HOSTNAME

package {'nginx':
  ensure   => 'installed',
  provider => 'apt',
}

$str = "server {
  \tlisten 80 default_server;
  \tlisten [::]:80 default_server;\n
  \troot /var/www/html;\n
  \tindex index.html index.htm index.nginx-debian.html;\n
  \tserver_name nyandi.tech;\n
  \tadd_header X-Served-By \$hostname;\n
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
  ensure  => 'running',
  enable  => 'true',
  restart => 'service nginx restart',
}
