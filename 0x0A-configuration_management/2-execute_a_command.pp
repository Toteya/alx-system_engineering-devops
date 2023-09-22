# This puppet manifest kills a process called 'killmenow'
exec { 'pkill':
  command => 'pkill killmenow',
  path    => '/usr/bin/'
}
