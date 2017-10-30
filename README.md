# twix #

### Intro ###
Simple project that extracts user tweets to csv / json <br>
based on the gist of [yanofsky](https://gist.github.com/yanofsky/5436496)

### Installation ###
in your terminal:

    > pip install twix 
    
### Twitter API Keys ###

1. Go to [twitter developers](https://dev.twitter.com/)
2. Click on "Sign In" in the upper-right corner.
    * There is a link to sign up under the username field if you do not already have a Twitter account.
    * If you sign up for a new account, you'll have to confirm your email before you can get an API key.
3. Enter your credentials and sign in.
4. Back at [twitter developers](https://dev.twitter.com/), click on your avatar in the upper-right corner, then My Applications.
5. Click on "Create a new application".
6. Fill out the information, agree to the Rules of the Road, do the captcha, and click on "Create your Twitter application".
7. In the application page that comes up next, copy down the **Consumer key** and **Consumer secret**. This is half of the key info.
8. Click on "Create my access token" at the bottom of the application page, under "Your access token".
9. (You may have to refresh the page first) Now under "Your access token", copy down your **Access token** and **Access token secret**.
	
### Examples ###

```python
from twix.tweets_extractor import TweetsExtractor
    
te = TweetsExtractor('your_consumer_key', 'your_consumer_secret', 'your_access_token', 'your_access_token_secret')
te.get_all_tweets(screen_name='netanyahu', fmt='csv', path='../bb.csv')
```

### Contact ###
[Tal Peretz](https://www.linkedin.com/in/tal-per/)





