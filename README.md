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

## twitter.GetMentions 

returns an array of tweets from which we create a Mention object with user=user.screen_name, text=text and id=id

```
{"created_at": "Sun Nov 16 17:20:22 +0000 2014",

 "id": 534033245575213056,

 "id_str": "534033245575213056",

 "in_reply_to_screen_name": "donpeat",

 "in_reply_to_status_id": 317339030104715264,

 "in_reply_to_user_id": 158357978,

 "lang": "en",

 "text": "@reporterdonpeat @MyProfMakes So when is he going to write a book?",

 "user": {"screen_name": "throwitinmyhat",      "statuses_count": 17117}}
```
