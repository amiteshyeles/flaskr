from setuptools import find_packages, setup

# This is where we describe the project and the files belonging to it.
setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)