===============================
{{ cookiecutter.service_name }}
===============================

{{ cookiecutter.service_description}}


Quickstart
----------


Then run the following commands to bootstrap your environment.


```
pip install -r requirements/dev.txt
python manage.py server
```


Deployment
----------

In your production environment, make sure the ``SETTINGS`` environment variable is set to ``config.Config``.


Shell
-----

To open the interactive shell, run ::

```
python manage.py shell
```

By default, you will have access to ``app``

