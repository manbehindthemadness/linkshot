from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='linkshot',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
        ],
    },
    author='Manbehindthemadness',
    author_email='manbehindthemadness@gmail.com',
    description='Manage unified linked files',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/manbehindthemadness/linkshot',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.5',
)
