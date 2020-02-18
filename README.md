# Docker image for Eve REST API framework.

[![Build Status](https://travis-ci.org/urbica/docker-eve.svg?branch=master)](https://travis-ci.org/urbica/docker-eve)

[Eve](http://python-eve.org) is an open source Python REST API framework designed for human beings. It allows to effortlessly build and deploy highly customizable, fully featured RESTful Web Services.

## Usage

```shell
docker run -p 5000:5000 -v $(pwd)/example.settings.py:/usr/src/app/settings.py urbica/eve
```

...or using docker-compose

```shell
docker-compose up
```
