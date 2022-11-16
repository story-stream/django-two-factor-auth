from setuptools import setup, find_packages

setup(
    name='django-two-factor-auth',
    version='1.0.0',
    description='Complete Two-Factor Authentication for Django',
    long_description=open('README.rst').read(),
    author='Bouke Haarsma',
    author_email='bouke@webatoom.nl',
    url='https://github.com/Bouke/django-two-factor-auth',
    download_url='https://pypi.python.org/pypi/django-two-factor-auth',
    license='MIT',
    packages=find_packages(exclude=('example', 'tests')),
    install_requires=[
        'Django>=1.4.2,<1.8',
        'django_otp>=0.2.0,<0.3.0',
        'qrcode>=4.0.0,<5.0.0',
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Security',
        'Topic :: System :: Systems Administration :: Authentication/Directory',
    ],
)
