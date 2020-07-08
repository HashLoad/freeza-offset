import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="freeza-offset",
    version="1.0.1",
    author="HashLoad team",
    description="Spark stream consumption commit in kafka consumer group",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HashLoad/freeza-offset",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    install_requires=["kafka-python"],
    python_requires='>=3.6',
)