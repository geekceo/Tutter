from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='Tutter',
  version='1.0',
  author='Tagir Khalilov',
  author_email='khalilov.tg@gmail.com',
  description='A convenient module for serialization and validation of data',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/geekceo/Tutter',
  packages=find_packages(),
  install_requires=['json'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='json serialization validation pydantic schemas templates data',
  project_urls={
    'GitHub': 'https://github.com/geekceo'
  },
  python_requires='>=3.7'
)