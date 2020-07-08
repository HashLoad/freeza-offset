# freeza-offset

![freeza-logo](freeza-logo.png)

## What is it?

**freeza-offset** is a Python package that provides a simple way to commit the offset consumed by Spark Streaming in Kafka's ConsumerGroup.

## Main Features
Here are just a few of the things that freeza-offset does well:

  - Commits the offset consumed in kafka
  - Tracking Spark consumption lag at Kafka
  - The offset is not just in control of the spark

## Where to get it
The source code is currently hosted on GitHub at:
https://github.com/HashLoad/freeza-offset

Binary installers for the latest released version are available at the [Python package index](https://pypi.org/project/freeza-offset) and on conda.

```sh
# conda
conda install freeza-offset
```

```sh
# or PyPI
pip install freeza-offset
```

## Dependencies
- [kafka-python](https://pypi.org/project/kafka-python)


## Installation from sources

In the `freeza-offset` directory (same one where you found this file after
cloning the git repo), execute:

```sh
python setup.py install
```

## License
[MIT](LICENSE)

## Notebook Example:


## Getting Help

For usage questions, the best place to go to is open [new issue](https://github.com/HashLoad/freeza-offset/issues/new)

## Contributing to freeza-offset [![Open Source Helpers]

All contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome.
