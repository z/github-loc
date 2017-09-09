from setuptools import setup
from setuptools import find_packages
from githubloc import __author__, __email__, __url__, __license__, __version__, __summary__, __keywords__

with open('README.md') as f:
    readme_contents = f.read()

setup(
    name='githubloc',
    version=__version__,
    description=__summary__,
    long_description=readme_contents,
    author=__author__,
    author_email=__email__,
    url=__url__,
    license=__license__,
    packages=find_packages(exclude=('tests', 'docs')),
    package_data={'': ['LICENSE', 'README.md', 'config/*']},
    include_package_data=True,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points={
       'console_scripts': [
          'github-loc = githubloc.cli:main'
       ]
    },
    keywords=__keywords__,
    classifiers=[
        'Intended Audience :: End Users/Desktop',

        'License :: OSI Approved :: MIT License',

        'Environment :: Console',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)