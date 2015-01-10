service-in-a-box
==================

###Note still needs a few tweaks to truly run out of the box.
######TODO - add some post hooks to try and semi-automate the oauth config?
######TODO - more post hooks for bower install?

A template for flask services using [cookiecutter](https://github.com/audreyr/cookiecutter). This cookie cutter template has been heavily influenced by [cookiecutter-flask](https://github.com/sloria/cookiecutter-flask)

####How to use it

Install cookiecutter (in it's own virtualenv would be a smashing idea)
```
pip install cookiecutter
```

then run:

```
cookiecutter https://github.com/ashimali/service-in-a-box.git
```

You will be prompted to answer some basic questions about your service and application. Also what registry you want to use and the permissions you require on that registry.


####What happens next

cd into the newly create directory for the application.

Use bower to install front end static assets
```
bower install
```
This will 3rd party static dependencies to static/vendor

Create a virtualenv for your new app
```
mkvirtualenv --python=/path/to/required/python/version [appname]
```

Install python requirements.
```
pip install -r requirements/dev.txt
```

Once that this all done you can
```
python manage.py server
```
and have a look at http://localhost:5000


#### License
MIT
