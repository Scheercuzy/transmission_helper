from setuptools import setup, find_packages


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    install_requires=[
        "appdirs==1.4.4",
        "apscheduler==3.6.3",
        "attrs==20.2.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "black==19.10b0; python_version >= '3.6'",
        "cached-property==1.5.2",
        "cerberus==1.3.2",
        "certifi==2020.6.20",
        "chardet==3.0.4",
        "click==7.1.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "colorama==0.4.4; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "distlib==0.3.1",
        "flask==1.1.2",
        "idna==2.10; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "importlib-metadata==2.0.0; python_version < '3.8'",
        "itsdangerous==1.1.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "jinja2==2.11.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "markupsafe==1.1.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "orderedmultidict==1.0.1",
        "packaging==20.4; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "pathspec==0.8.0",
        "pep517==0.9.1",
        "pip-shims==0.5.3; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "pipenv-setup==3.1.1",
        "pipfile==0.0.2",
        "plette[validation]==0.2.3; python_version >= '2.6' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "pyparsing==2.4.7; python_version >= '2.6' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "python-dateutil==2.8.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "pytz==2020.1",
        "pyyaml==5.3.1",
        "regex==2020.10.15",
        "requests==2.24.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "requirementslib==1.5.13; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "six==1.15.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "toml==0.10.1",
        "tomlkit==0.7.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "typed-ast==1.4.1",
        "typing==3.7.4.3; python_version < '3.7'",
        "tzlocal==2.1",
        "urllib3==1.25.11; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4' and python_version < '4'",
        "uwsgi==2.0.19.1",
        "vistir==0.5.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "werkzeug==1.0.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "wheel==0.35.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "zipp==3.3.1; python_version < '3.8'",
    ],
    name="transmission_sync",
    version="0.2a",
    python_requires=">=3.5",
    description="""The program that will take care
    of my transmission setup""",
    long_description=readme(),
    url="https://github.com/Scheercuzy/transmission_helper",
    author="MX",
    author_email="maxi730@gmail.com",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": ["transmission_helper = transmission_helper.__main__:main"]
    },
)
