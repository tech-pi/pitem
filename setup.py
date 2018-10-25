from setuptools import setup, find_packages

setup(name='pitem',
      version='0.0.1',
      description='Easy data model',
      url='https://github.com/tech-pi/pitem',
      author='Hong Xiang',
      author_email='hx.hongxiang@gmail.com',
      license='Apache',
      packages=find_packages(),
      install_requires=[
          'attrs>=18.1.0',
          'marshmallow>=3.0.0',
          'flask>=1.0.0',
          'sqlalchemy>=1.2.12'
      ],
      zip_safe=False)
