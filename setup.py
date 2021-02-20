import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tcolor",
    version="1.0.0",
    author="ammarsys",
    author_email="amarftw1@gmail.com",
    description="tool to print colored text messages, aswell to markup them",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ammar-sys/tcolor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
