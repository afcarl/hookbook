from setuptools import setup

exec(open('hookbook/version.py').read())

setup(
    name='hookbook',
    version=version,
    packages=['hookbook'],
    description='Library for reading Github, Bitbucket, Gitlab webhook data',
    author='Bradley Cicenas',
    author_email='bradley.cicenas@gmail.com',
    url='https://github.com/bcicen/hookbook',
    install_requires=requirements,
    license='http://opensource.org/licenses/MIT',
    classifiers=(
        'License :: OSI Approved :: MIT License ',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Development Status :: 5 - Production/Stable',
    ),
    keywords='github bitbucket gitlab webhook devops',
)
