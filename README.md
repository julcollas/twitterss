# Twitterss - Get twitter as RSS feeds

## Dependencies

You do need:
A devlopper twitter app to get Consumer Key and Acces Token


## Running
### Using docker

Build & run

```shell
docker build . -t twitterss
docker run -d \
--name=twitterss \
-e TWITTER_CONSUMER_KEY=<twitter_consumer_key> \
-e TWITTER_CONSUMER_SECRET=<twitter_consumer_secret> \
-e TWITTER_ACCESS_TOKEN=<twitter_access_token> \
-e TWITTER_ACCESS_TOKEN_SECRET=<twitter_access_token_secret> \
-e PORT=1234 \
-p 1234:1234 \
twitterss
```

## Configuration
### ENV Variables

- `TWITTER_CONSUMER_KEY`
- `TWITTER_CONSUMER_SECRET`
- `TWITTER_ACCESS_TOKEN`
- `TWITTER_ACCESS_TOKEN_SECRET`
- `PORT`

## Usage
- <http://localhost:1234/home>
- <http://localhost:1234/btonight?retweet=false&replies=false>
