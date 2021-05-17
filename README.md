# Django UI Components
> *Reusable UI components for your Django templates*

[![PyPI](https://img.shields.io/pypi/v/django-uicomponents?color=blue)](https://pypi.org/project/django-uicomponents/)
[![Build Status](https://travis-ci.org/koenwoortman/django-uicomponents.svg?branch=main)](https://travis-ci.org/koenwoortman/django-uicomponents)


## Usage

1. Create a component file, such as `./templates/components/button.html`.

```html
<button class="px-4 py-2 font-semibold rounded-lg shadow text-sm text-white
  {% if variant == 'danger' %}
    bg-red-500 hover:bg-red-400
  {% elif variant == 'success' %}
    bg-green-500 hover:bg-green-400
  {% else %}
    bg-blue-500 hover:bg-blue-400
  {%endif%}
">
  {{ text }}
</button>
```

2. Load `components` at the top of your template and include the UI component by using the `component` template tag possibly with keyword arguments.

```html
{% load static %}
{% load components %}

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Django UI Components</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
    <link rel="icon" type="image/x-icon" href="{% static 'favicon.ico' %}">
  </head>

  <body class="bg-gray-50 flex items-center min-h-screen justify-center">
    {% component 'button.html' text="Delete" variant="danger" %}
    {% component 'button.html' text="Save" variant="success" %}
    {% component 'button.html' text="Ok" %}
  </body>
</html>
```

3. This results in three button variations.

<div align="center">
  <div>
    <img src="https://github.com/koenwoortman/django-uicomponents/raw/main/media/screencapture.png" alt="Example screenshot">
  </div>
</div>

## Install

Install the package from [pypi](https://pypi.org/project/django-uicomponents/).

```
$ pip install django-uicomponents
```

Add `django_uicomponents` to your INSTALLED_APPS.

```python
# settings.py

INSTALLED_APPS = [
    ...
    'django_uicomponents',
    ...
]
```

## Settings

| Option               | Description                                                          | Default        |
| :------------------- | :------------------------------------------------------------------- | :------------- |
| **`COMPONENTS_DIR`** | Directory inside your template dir from which components are loaded. | `'components'` |


## License

Released under the [MIT license](https://github.com/koenwoortman/django-uicomponents/blob/main/LICENSE).
