import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CapPy-Python",
    version="0.0.5",
    author="GEONE",
    author_email="geonegames@gmail.com",
    description="Python package for easy window capturing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GE0NE/CapPy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: Microsoft :: Windows :: Windows 8.1",
        "Operating System :: Microsoft :: Windows :: Windows 8",
        "Operating System :: Microsoft :: Windows :: Windows 7",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    install_requires=[
        "numpy>=1.15.0",
        "pillow>=5.0.0",
        "pywin32>=224",
        "psutil>=5.4.3"
    ],
)