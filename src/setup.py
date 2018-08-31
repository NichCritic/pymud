import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyMud",
    version="0.0.1",
    author="Nicholas Aelick",
    author_email="n.aelick@gmail.com",
    description="A MUD engine build in python on top of Tornado",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NichCritic/pymud",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
