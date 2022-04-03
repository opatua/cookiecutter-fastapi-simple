# cookiecutter-fastapi-simple

A Simple FastAPI template for cookiecutter.

## Structure and Feature
```
|--{your_app_name}
    |--app
        |--api
        |   |--v1
        |        |--endpoints
        |        |  |--hello_word.py (your endpoints should be in this folder)
        |        |--api_router.py
        |--core
            |--config.py
```

> This template support Docker

## Use it now
----------

    $ pip install cookiecutter
    $ cookiecutter https://github.com/opatua/cookiecutter-fastapi-simple.git

You will be asked about your basic info (name, app name, etc.). This info will be used in your new project.

## License
-------

MIT licensed.

Please change the license accordingly. Currently, I use MIT license.