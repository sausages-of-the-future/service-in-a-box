service-in-a-box
==================

###Note still needs a few tweaks to truly run out of the box.
######TODO - add some post hooks to try and semi-automate the oauth config?

A template for flask services using [cookiecutter](https://github.com/audreyr/cookiecutter). This cookie cutter template has been heavily influenced by [cookiecutter-flask](https://github.com/sloria/cookiecutter-flask)

####How to use it

Install cookiecutter (in it's own virtualenv would be a smashing idea)
```
pip install cookiecutter
```

then run:

```
cookiecutter https://github.com/sausages-of-the-future/service-in-a-box.git
```

You will be prompted to answer some basic questions about your service and application. Also what registry you want to use and the permissions you require on that registry.


####What happens next

Create a virtualenv for your new app
```
mkvirtualenv --python=/path/to/required/python/version [appname]
```

cd into application directory and run
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