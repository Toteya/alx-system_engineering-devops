# This puppet manifest makes changes the ssh config file to:
# 1. use the private key ~/.ssh/school
# 2. refuse to authenticate using a password

$str = "Host *
  \tPasswordAuthentication No
  \tIdentityFile ~/.ssh/school
"

file { 'config':
  ensure  => 'present',
  content => $str,
  path    => '/home/ubuntu/.ssh/config',
}
