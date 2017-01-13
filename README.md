# Twitter Bot (@myprofmakes)

# requirements

[python-twitter](https://github.com/bear/python-twitter)

sudo pip3 install python-twitter


##GetMentions 

returns an array of tweets:

`
{"created_at": "Sun Nov 16 17:20:22 +0000 2014",
 "id": 534033245575213056,
 "id_str": "534033245575213056",
 "in_reply_to_screen_name": "donpeat",
 "in_reply_to_status_id": 317339030104715264,
 "in_reply_to_user_id": 158357978,
 "lang": "en",
 "source": "<a href=\"https://about.twitter.com/products/tweetdeck\" rel=\"nofollow\">TweetDeck</a>",
 "text": "@reporterdonpeat @MyProfMakes So when is he going to write a book?",
 "user": {"created_at": "Wed Nov 06 04:24:11 +0000 2013",
          "default_profile": true,
          "description": "If your family tree doesn't fork, you might be a redneck. Genes & chromosomes",
          "favourites_count": 22104,
          "followers_count": 943,
          "friends_count": 931,
          "geo_enabled": true,
          "id": 2177337757,
          "lang": "en",
          "listed_count": 18,
          "location": "Toronto, Ontario",
          "name": "Christina",
          "profile_background_color": "C0DEED",
          "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
          "profile_banner_url": "https://pbs.twimg.com/profile_banners/2177337757/1414848989",
          "profile_image_url": "http://pbs.twimg.com/profile_images/528541667859521536/xcxYY2uu_normal.jpeg",
          "profile_link_color": "1DA1F2",
          "profile_sidebar_fill_color": "DDEEF6",
          "profile_text_color": "333333",
          "screen_name": "throwitinmyhat",
          "statuses_count": 17117}}
`
