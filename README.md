# Github_search_security

[![N|Solid](http://e-cyber.ee/wp-content/uploads/2019/04/cropped-8c1fd234-451d-4b95-ad13-0d561779eeaa-1.png)](http://e-cyber.ee/)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

"Github_search_security" is a tool use for monitoring leak sensitive information and alert in chat channel.

  - Writing with Python, bash.
  - Define information in separately text file.
  - Easy custom.

## Features

  - Get result newly and correctly, minimize rate false positive.
  - Show information clearly: project name, file name, link repo, code contain leak information,... 
  - Customize chat channel by input link in file "get_data.py" (eg. Hangout, Slack,...)
  - May be using crontab, so that monitoring real-time information leak in github


## Running
1. Setup file crontab with real-time running
```
32 */1 * * * sh /home/sgithub/scripts/github_search/get_search.sh > /var/log/sgithub_error.log 2>&1
```
2. In file get_data.py input link Hangouts for primary, log
```
# url for channel google hangouts
url_primary = "https://chat.googleapis.com/v1/spaces/AAAAjYF3XU0/messages?key=AIxxx"
url_loging = "https://chat.googleapis.com/v1/spaces/AAAA1EgMQ9U/messages?key=AIyyy"
url_test = "https://chat.googleapis.com/16DZUzJatIekyQScPisQ2V/messages?key=AIzzz"
```
3. In file keyword.txt input link maybe leak like staging, private, test,...
```
flickr.com
uit.edu.vn
```

If you want to run once. Let execute command:
```
$ sh get_search.sh
```

### Demo
![Leak link!](https://i.ibb.co/Jns40ct/github.png)


### Relates work:
- Multiple support for Chat channel using API.
- Having a dataset for script.




License
----

MIT

