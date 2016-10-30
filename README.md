# github-loc

A script to tell you how many lines have been committed by a user on github.

This script works with anonymous requests, but you will be [rate limited quickly](https://api.github.com/rate_limit). 

To increase your rate limit, [generate a personal access token](https://github.com/settings/tokens) and add into to `~/.githubloc.ini`.

You can probably run this 2-3 times before you get rate limited for 3 hours without a token.

#### Config (optional)

You'll need a personal access token (see link above).

```
python3 setup.py install
vim ~/.githubloc.ini
```

Replace `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` with your token.

#### Usage

```
usage: github-loc [-h] [--version] --user [USER] [--token [TOKEN]]

Count how many lines of code have been commited by a github user

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  --user [USER], -u [USER]
                        github username
  --token [TOKEN], -t [TOKEN]
                        github personal access token (overrides the one in
                        config.ini)
```


#### Example

```
github-loc --user z
```
