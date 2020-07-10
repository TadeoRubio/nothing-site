# nothing-site

## Website on Microservice to do Nothing

### Developer

Tadeo Rubio

### Overview

Some cases when you codes services for Google App Engine™ and you ready to deploy it, an error remember you that "My service can't deploy because the default service hasn't one version".

Maybe, the default service will be create later or by other team member now. Anyway, you don't want stop.

So, this simple code can help you (as a workaround), nothing-site creates the default service for Google App Engine™ with a Flask site, and for all requests you make them, all have the same response: *204 - NO CONTENT*

**By default handles the 404-Not Found to 204-No content.**

### Running on localhost

#### Recommended requirements

1. Python 3.7+
2. Virtualenv 20.0.26+
3. Flask 1.0.2

#### Steps

1. Clone the git
2. Make you virtual environment

                virtualenv -p python3 venv/
                source venv/bin/activate

3. Install the [requirements](requirements.txt)

                pip install -r requirements.txt

4. Run

                python main.py

### Samples

A request to the index:
> `tadeo@host$ curl -i http://localhost:8080/`

Result:
> `HTTP/1.0 204 NO CONTENT`\
> `Content-Type: application/json`\
> `Cache-Control: public, max-age=60,s-maxage=60 must-revalidate`\
> `X-Robots-Tag: none`\
> `Server: Werkzeug/1.0.1 Python/3.7.7`\
> `Date: Fri, 10 Jul 2020 03:32:32 GMT`

A request to a nonexistent resource:
> `tadeo@host$ curl -i http://localhost:8080/example/`

Result:
> `HTTP/1.0 204 NO CONTENT`\
> `Content-Type: text/html; charset=utf-8`\
> `Cache-Control: public, max-age=60,s-maxage=60,must-revalidate`\
> `X-Robots-Tag: none`\
> `Server: Werkzeug/1.0.1 Python/3.7.7`\
> `Date: Fri, 10 Jul 2020 03:32:53 GMT`\

### DEPLOY

Only execute:

                gcloud app deploy app.yaml

[See the deploy documentation for Google App Engine™](https://cloud.google.com/sdk/gcloud/reference/app/deploy)

### LICENSE

[See License](LICENSE)
