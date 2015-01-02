try:
    from setuptools import setup
except:
    from distutils.core import setup
    
config = {
    'description': 'My Project',
    'author': 'Oliver Muellerklein',
    'url': 'https://github.com/ShyneColdchain/FILENAME',
    'download_url': 'Where to download it.',
    'author_email': 'olivermuellerklein@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)