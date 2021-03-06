import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

setup(name='kotti_tinymce',
      version='0.1',
      description="TinyMCE plugins for Kotti",
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "License :: OSI Approved :: MIT License",
        ],
      author='',
      author_email='',
      url='http://pypi.python.org/pypi/kotti_tinymce',
      keywords='tinymce image browser kotti cms pylons pyramid',
      license="MIT",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=['Kotti', 'pytest'],
      )
