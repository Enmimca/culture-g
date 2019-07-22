import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

with open('LICENSE') as f:
    license = f.read()

setuptools.setup(
    name="Culture-g",
    version="1.0.1",
    author="Enminca, Th0rgal",
    author_email="emma.esquirol2002@gmail.com, thomas.marchand44@gmail.com",
    description="A package created to manage our game Culture-g",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Enminca/culture-g",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)