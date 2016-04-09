# github-loc

A script to tell you how many lines have been committed by a user on github.

This script works with anonymous requests, but you will be [rate limited quickly](https://api.github.com/rate_limit). 

To increase your rate limit, [generate a personal access token](https://github.com/settings/tokens) and add into to `config.ini`.

#### Config (optional)

You'll need a personal access token (see link above).

```
cp example.config.ini config.ini
```

Replace `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` with your token.

#### Usage

```
usage: app.py [-h] --user [USER] [--token [TOKEN]]

Count how many lines of code have been commited by a github user

optional arguments:
  -h, --help            show this help message and exit
  --user [USER], -u [USER]
                        github username
  --token [TOKEN], -t [TOKEN]
                        github personal access token
```


#### Example

```
python3 app.py --user z
```
