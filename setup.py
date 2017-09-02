from setuptools import setup

setup(
    name='click-example-complex',
    version='1.0',
    packages=['slogger', 'slogger.commands'],
    include_package_data=True,
    install_requires=[
        'click',
        'tinyDB',
    ],
    entry_points='''
        [console_scripts]
        slog=slogger.cli:cli
    ''',
)
