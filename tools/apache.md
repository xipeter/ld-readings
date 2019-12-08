# apache

# INSTALL
ubuntu下apt-get即可

# ubuntu下的多域名反向代理
参考[apache2反向代理](https://www.cnblogs.com/xiaomifeng0510/p/9020738.html)。
核心在于/etc/apache2/sites-available/\*.conf里配置VirtualHost的时候，打开ServerName配置项，配置为需要反向代理的域名，每个域名一个配置文件，这样每个配置文件就都有自己的反向代理映射规则了。
```
<VirtualHost *:80>
  # The ServerName directive sets the request scheme, hostname and port that
  # the server uses to identify itself. This is used when creating
  # redirection URLs. In the context of virtual hosts, the ServerName
  # specifies what hostname must appear in the request's Host: header to
  # match this virtual host. For the default virtual host (this file) this
  # value is not decisive as it is used as a last resort host regardless.
  # However, you must set it for any further virtual host explicitly.
  ServerName ld-readings.littleding.cn

  ServerAdmin webmaster@localhost
  DocumentRoot /var/www/html

  # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
  # error, crit, alert, emerg.
  # It is also possible to configure the loglevel for particular
  # modules, e.g.
  #LogLevel info ssl:warn

  ErrorLog ${APACHE_LOG_DIR}/error.log
  CustomLog ${APACHE_LOG_DIR}/access.log combined

  # For most configuration files from conf-available/, which are
  # enabled or disabled at a global level, it is possible to
  # include a line for only one particular virtual host. For example the
  # following line enables the CGI configuration for this host only
  # after it has been globally disabled with "a2disconf".
  #Include conf-available/serve-cgi-bin.conf

  ProxyRequests Off 
  ProxyMaxForwards 100 
  ProxyPreserveHost On
  ProxyPass / http://127.0.0.1:4000/
  ProxyPassReverse / http://127.0.0.1:4000/
  <Proxy *>
    Order Deny,Allow
    Allow from all
  </Proxy>

</VirtualHost>

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet
```

# 参考资料
* [apache2反向代理](https://www.cnblogs.com/xiaomifeng0510/p/9020738.html)
