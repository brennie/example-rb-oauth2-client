"""Setup example-rb-oauth2-client."""

from setuptools import setup, find_packages


setup(
    name='example-rb-oauth2-client',
    version='0.1.0',
    description='An example OAuth2 client for Review Board',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'Django >=1.11,<1.12',
        'social-auth-core >=1.2.0',
        'social-auth-app-django >=1.1.0',
    ],
)

