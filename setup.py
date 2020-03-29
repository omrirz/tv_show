import setuptools

from tv_show import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='tv_show',
    version=__version__,
    author='Netflix',
    author_email='net.flix@netflix.com',
    url='https://github.com/netflix/tv_show.git',
    description='Utilities for TV show',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "'Operating System :: POSIX",
    ],
    python_requires='>=3.6',
)
