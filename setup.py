from setuptools import setup


setup(
    name='beetle-sample-plugin',
    version='0.0.1',
    author='Kasper Jacobsen',
    author_email='k@mackwerk.dk',
    license='MIT',
    keywords='',
    packages=[
        'beetle_sample'
    ],
    classifiers=[
        '',
    ],
    install_requires=[
        'beetle',
    ],
    dependency_links=[
        'git+ssh://git@github.com/Dinoshauer/beetle.git#egg=beetle',
    ],
)
