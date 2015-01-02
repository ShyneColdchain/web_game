try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description': 'web_game',
    'author': 'Oliver Muellerklein',
    'url': 'https://github.com/ShyneColdchain/web_game',
    'download_url': 'Where to download it.',
    'author_email': 'olivermuellerklein@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['web_game'],
    'scripts': ['bin/run_game.py'],
    'name': 'game'
}

setup(**config)