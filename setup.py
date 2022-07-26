import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lawsplit",                             # This is the name of the package
    version="0.0.1",                             # The initial release version
    author="Pritish Wadhwa",                     # Full name of the author
    description="LawSplit: A smart legal text sentence splitter",
    # Long description read from the the readme file
    long_description=long_description,
    long_description_content_type="text/markdown",
    # List of all python modules to be installed
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["lawsplit"],                # Name of the python package
    # Directory of the source code of the package
    package_dir={'': 'lawsplit/src'},
    # Install other dependencies if any
    install_requires=["pysbd", "re"]
)
