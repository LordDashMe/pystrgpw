from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pystrgpw',
    version='1.0.0',
    description='A simple package that generates random characters and can be used for strong passwords.',
    url='https://github.com/LordDashMe/pystrgpw',
    author='Joshua Clifford Reyes',
    author_email='reyesjoshuaclifford@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_dir={'': 'src'},
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    install_requires=[],
    extras_require={
        'dev': [
            'pytest'
        ]
    }
)
