try:
    from setuptools import setup
except:
    from distutils.core import setup
    
config = {
    'description': 'Automated testing',
    'author': 'Oliver Muellerklein',
    'url': 'https://github.com/ShyneColdchain/FILENAME',
    'download_url': 'Where to download it.',
    'author_email': 'olivermuellerklein@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)