# Use Puppet to automate the task of creating a custom HTTP header response

import 'puppetlabs/stdlib/file_line'

exec {'update':
  command => '/usr/bin/apt-get update',
}
-> package {'nginx':
  ensure => 'present',
}
-> file_line { 'http_header':
  path  => '/etc/nginx/sites-available/default',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}
-> exec {'run':
  command => '/usr/sbin/service nginx restart',
}
