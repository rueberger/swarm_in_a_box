""" Setup script
"""

from setuptools import setup

setup(
    name='foo',
    version='0.1',
    author='Andrew Berger',
    author_email='andbberger@gmail.com',
    description='Example python project',
    url='https://github.com/rueberger/config_zoo/projects/foo',
    packages=['foo'],
    python_requires='>=3.5',
    install_requires=[
        'eliot'
        'hypothesis',
        'hypothesis[pytz]',
        'nose'
        'pytz'
    ],
    entry_points={
        'console_scripts': [
            'foo=foo.daemon:main'
        ]
    }
)
