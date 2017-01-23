# Twitter Bot (@myprofmakes)

## API Keys (apps.twitter.com)

Put ENV Variables in /etc/sysconfig/myprofbot
:

```
AT='ACCESS-TOKEN'
ATS='ACCESS-TOKEN-SECRET'
CK='CONSUMER-KEY'
CS='CONSUMER-SECRET'
```


## run as service 

chmod +x bot.py

change paths in myprofbot service to match absolute location of this repo

    ExecStart and WorkingDirectory

sudo cp myprofbot.service /etc/systemd/system

sudo systemctl enable myprofbot.service

sudo systemctl preset myprofbot.service

### service commands

sudo service myprofbot start|stop|restart|status



# requirements

`sudo apt install python-pip3` 

redis:

```
wget http://download.redis.io/redis-stable.tar.gz

tar xvzf redis-stable.tar.gz

cd redis-stable

make install
```

[python-twitter](https://github.com/bear/python-twitter)

`sudo pip3 install python-twitter redis`

