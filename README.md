# django-pydoc

`pydoc` is a built in Python tool for documenting your python modules. But `pydoc` does not work as expected with your Django module unless you explicitely prepare Django before executing pydoc.

The `django_pydoc` does just that, preparing the Django configuration before executing `pydoc`.

## How to use `django-pydoc`
Place the `django_pydoc.py` file in your Django project (you can place in next to your `manage.py`). Based on the location of your `settings.py` file, you may need to update the value of `DJANGO_SETTINGS_MODULE` (By default it is assumed that `settings.py` is located in the same location of `manage.py`).

After you have the `django_pydoc.py` file in position, you can call regular `pydoc` commands through it.
For example: instead of: ```pydoc -p 1234``` command you can write: ```python django_pydoc.py -p 1234```.

You can use all the `pydoc` commands with `django-pydic` in the above process.

## More About `pydoc` Commands
Please read [official documentation of `pydoc`](https://docs.python.org/2/library/pydoc.html) to learn about the functionality and commands.
