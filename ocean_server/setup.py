"""
setup module for ocean
"""

from os.path import dirname, join, realpath
from setuptools import setup, find_packages

cwd = dirname(realpath(__file__))
with open(join(cwd, 'ocean/version.py')) as version_file:
    for line in version_file:
        if line.startswith('__version_info__'):
            exec(line)

long_description = ('An experimental web server for my personal website. This '
                    'project uses kyoukai, which is a web framework built '
                    'around the new async/await syntax introduced in Python '
                    '3.5')

setup(
    name='ocean',
    version='.'.join([str(ver) for ver in __version_info__]),
    description='A personal web server built using kyoukai and async/await',
    long_description=long_description,
    url='https://www.github.com/mplanchard/ocean',
    author='Matthew Planchard',
    author_email='mplanchard@ihiji.com',
    classifiers=[
        'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        # 'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
    ],
    keywords=('web', 'server', 'async', 'kyoukai', 'python3.5'),
    packages=find_packages(exclude=['*.tests', '*.tests.*']),
    install_requires=['kyoukai', 'sqlalchemy'],
)
