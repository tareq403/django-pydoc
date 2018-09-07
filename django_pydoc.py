"""
    Created by tareq on 8/17/18
"""
import os
import django
import pydoc

__author__ = "Tareq"

# Prepare Django before executing pydoc command
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings' # Change the value according to your django settings path
django.setup()

# Now executing pydoc
pydoc.cli()

