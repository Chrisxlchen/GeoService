from setuptools import setup

setup(
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ], install_requires=['requests', 'PyYAML']
)