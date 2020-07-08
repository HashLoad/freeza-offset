import setuptools

exec(open('freeza/version.py').read())

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="freeza-offset",
    version=__version__,
    author="HashLoad team",
    author_email="rodrigo@rbernardi.dev, lviecelli199@gmail.com",
    description="Spark stream consumption commit in kafka consumer group",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HashLoad/freeza-offset",
    packages=setuptools.find_packages(),
    keywords="spark spark-streaming kafka kafka-commit kafka-offset-commits databricks",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    install_requires=["kafka-python"])