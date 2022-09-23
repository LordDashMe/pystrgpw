# pystrgpw

A simple package that generates random characters and can be used for strong passwords.

<a href="https://app.travis-ci.com/LordDashMe/pystrgpw">
  <img src="https://img.shields.io/travis/LordDashMe/pystrgpw?style=for-the-badge" />
</a>

## Requirements

- Python >= 3.9.x

## Install

To install the package, use the command below:

```
pip install pystrgpw
```

## Usage

The basic usage of this package is explained below.

```python
import pystrgpw

strgpw = pystrgpw.Generator()

# Set the character length output.
strgpw.length(25)

# Execute the generate process.
strgpw.generate()

# Get the generated output and print "0123456789abcdefghijklmn..."
print(strgpw.get()) 
```

## To Contribute

### Development

To prepare the dev environment, you need to run the command below in your virtualenv:

```
pip install -e .[dev]
```

#### Unit Testing

To run the test cases, use the command below:

```
pytest -s --verbose
```

#### Publishing the Package

To build the source code using ```bdist_wheel``` and ```sdist```, use the command below:

```
python setup.py bdist_wheel sdist
```

To publish the source distribution on [pypi.org](https://pypi.org/) (pip), run the command below:

  - Install the twine:

    ```
    pip install twine
    ```

  - Execute twine upload:

    ```
    twine upload dist/*
    ```

#### When using Docker as Local Environment Setup

Using Docker compose setup, we need to make sure to execute the commands below to avoid environment issues:

```
apk add --update --no-cache --virtual .tmp-build-deps gcc libc-dev linux-headers postgresql-dev libffi-dev
```

## License

This package is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).
