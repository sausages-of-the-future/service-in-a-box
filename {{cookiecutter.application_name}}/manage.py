#!/usr/bin/env python{{cookiecutter.python_version}}
# -*- coding: utf-8 -*-
import os
from flask.ext.script import Shell, Server, Manager

from {{cookiecutter.application_name}} import app

manager = Manager(app)
manager.add_command('server', Server())

if __name__ == '__main__':
    manager.run()

