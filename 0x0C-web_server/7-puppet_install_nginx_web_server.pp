# Nginx configuration with Puppet
class { 'nginx': }

# Remove default Nginx configuration
nginx::resource::server { 'default':
  ensure => absent,
}

# Create custom index.html with Hello World!
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  mode    => '0644',
}

# Configure Nginx server with redirect
nginx::resource::server { 'hello_world':
  ensure               => present,
  listen_port          => 80,
  server_name         => ['_'],
  www_root             => '/var/www/html',
  index_files          => ['index.html'],
  location_cfg_append  => {
    'rewrite' => '^/redirect_me https://www.example.com permanent',
  },
}

# Ensure Nginx service is running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Class['nginx'],
}
