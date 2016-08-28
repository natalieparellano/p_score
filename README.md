# Approach

I decided to work with the Twitter API. The basis of my very simple and inaccurate model is that businesses with a greater number of twitter mentions are likely to be more well established, and thus lower risk. 

# Challenges

Fuzzy matching: matching on name (owner or business) is inherently inaccurate. We could attempt a fuzzy match using some combination of name / geography / etc. but it will never be perfect. E.g., if we execute a search on "Ray's Pizza" the tweets returned could relate to any number of pizza shops in New York City. It might be concerning to use data where there is a low degree of certainty of its relevance to the actual business being considered for credit.

It might be possible to ask the applicant to provide their Twitter handle, but this has its own issues including explaining the use of this information to the applicant, and the extra burden of having another form field to fill out, which may affect completion rates. For now, I have chosen to use the business' URL as the unique identifier to search for. 

Another challenge - the API rate limits imposed by Twitter and formatting of the result set. Each query returns a maximum of 100 records (sorted by recency) where all records were created within the last 7 days. This naturally imposes some limits on the kind of analysis that is possible. 

I've chosen to look for a maximum of 1000 tweets per applicant. This means (at most) 10 API calls per applicant. I believe the rate limit is 18k calls per 15 minutes, which doesn't pose an issue for now, but may be something to consider further in the future. 

One other caveat to note - the approach that I have taken (described [here](https://dev.twitter.com/rest/public/timelines) in the Twitter documentation) is to query the API, note the least recent record id in the result set (call it max_id), then query the API again while specifying that the results should all be less recent than the max_id specified (less than or equal to max_id - 1). This ensures that no duplicate data is returned. As the ids used by Twitter are all very large, we need to ensure that any machines running the code are using 64-bit precision to avoid errors when doing the subtraction. 

# How the code is structured

I have used the [TwitterAPI](https://github.com/geduldig/TwitterAPI) library to support querying the Twitter endpoints. This needs to be installed with pip. I load credentials from a config file, structured as shown, but removed from this git repository to avoid exposing my credentials.

config/twitter_secret.json
 ```
{
  "twitter_consumer_key": "XXX",
  "twitter_consumer_secret": "XXX",
  "twitter_token": "XXX",
  "twitter_token_secret": "XXX"
}
```

There are 3 classes in use here - TwitterService, which is responsible for making API calls and returning data, ScoreService, which is responsible for ingesting data obtained from the API (in this case, the total number of tweets) and returning a score. I've chosen a simple metric - the log of the total number of tweets - to grade applicants on a scale from 0 to 3. I then transform that grade into a number between 0 and 1. 

The last class is ScoreManager, which is responsible for calling TwitterService and ScoreService in succession, and would ultimately return the score to the calling service. 

# Possible optimizations

Right now a lot of information is being discarded - it would be nice to look at the actual content of tweets vs. just the total number. Some sort of textual analysis, e.g., sentiment analysis, might be helpful to understand how the tweets correlate to the health of the business. 

Another thing to consider might be the number of unique users who are tweeting about the business. This would help avoid data from a handful of very active users skewing the result set. 

As for the actual code, it would be good to handle errors returned by the API - such as logging the error, retrying after a suitable period, or returning a message to the end user.

Finally, while I have written some tests, they are just the bare minimum required to write the code in a test driven way. It would be good to add more assertions, ensuring all edge cases are covered. 
