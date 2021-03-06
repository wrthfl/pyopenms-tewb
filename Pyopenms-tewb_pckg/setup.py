import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyopenms-tewb",
    version="0.0.2",
    author="Sevvalli Thavapalan, Till Englert, Fabian Wurth, Philipp Baltik",
    author_email="sevvalli.thavapalan@student.uni-tuebingen.de",
    description="Package for pyopenms-tewb",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wrthfl/pyopenms-tewb",
    packages=setuptools.find_packages(include=['documentation', 'src',
                                    'Pyopenms-tewb_pckg',
                                    'license.txt', 'README.md']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
