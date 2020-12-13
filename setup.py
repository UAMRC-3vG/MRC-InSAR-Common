from setuptools import setup,find_packages

setup(
    name = 'MRC-InSAR-Common',
    version = '0.0.1',
    author = 'Xinyao(Alvin) Sun',
    author_email = 'xinyao1@ualberta.ca',
    packages = find_packages(),
    install_requires = [
        'numpy'
    ]
)
