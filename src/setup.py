from setuptools import setup, find_packages

setup(
  name      = "todobackend",
  version   = "0.1.0",
  description = "Todobackend Django REST service",
  packages = find_packages(),
  include_package_data = True,
  scripts = ["manage.py"],
  install_requires = ["asgiref == 3.2.3",
                      "autopep8 == 1.5",
                      "Django == 3.0.3",
                      "django-cors-headers == 3.2.1",
                      "djangorestframework == 3.11.0",
                      "mysqlclient == 1.4.6",
                      "pycodestyle == 2.5.0",
                      "pytz == 2019.3",
                      "sqlparse == 0.3.1",
                      "uwsgi == 2.0.18"
                      ],
  extras_require  = {
                      "test": [
                          "colorama == 0.4.3",
                          "coverage == 5.0.3",
                          "django-nose == 1.4.6",
                          "nose == 1.3.7",
                          "pinocchio == 0.4.2"
                      ]
                    } 
)
