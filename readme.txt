

####Troubleshooting

If something goes wrong, the first place to check is the log files. 



#####Nginx 

http access logs 
```
tail /var/log/nginx/access.log
```
http error logs 
```
tail /var/log/nginx/error.log
```

Nginx status
```
systemctl status nginx.service
```

#####Emperor

To see if the uWSGI process was spawned correctly
```
tail /var/log/uwsgi/emperor.log
```

If the emperor seems to be not working when you call start uwsgi run this:
```
/var/www/app/venv/bin/uwsgi --master --emperor /etc/uwsgi/vassals --die-on-term --uid www-data --gid www-data --logto /var/log/uwsgi/emperor.log

```
Now try to access via browser. If you see the page the problem is not emperor o uWSGI but the 'start' command


#####uWSGI
To see the all the dynamic content activity including the python print() and python error traces
```
tail /var/log/uwsgi/uwsgi.log
```



#### Static Files

Add the following rule to serve the Static files from avispa
```
location /static {
    root /var/www/app/;
}
```
As a result, all static files located at /var/www/app/static will be served by Nginx.

#### Sometimes you need to turn on and off a service:

Virtual Environment
```
$ deactivate
$ source /var/www/app/venv/bin/activate
```


Nginx 
```
$ /etc/init.d/nginx stop
$ /etc/init.d/nginx start
```

uWSGI
```
$ stop  uwsgi
$ start uwsgi
```

#### Hard Restarting the Machine
In case you need to restart the server you'll have to restart the virtual environment and all the services. Run the following commands:
```
$ source /var/www/app/venv/bin/activate
$ /etc/init.d/nginx start
$ start uwsgi 
```
