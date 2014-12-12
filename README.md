# navras

Contribution Pathways

## install

This assumes that you have already cloned the repo locally and installed `python-virtualenvwrapper`.

On first run you should create a new virtualenv

`mkvirtualenv navras -a [your_code_path]`

Activate your virtualenv and install requirements:

```
workon navras
pip install -r requirements/dev.txt
```

Set your enviromental variables:

`cp .env-dist .env`

Setup the database:

`./manage.py migrate`

And run the app

`./manage.py runserver`
