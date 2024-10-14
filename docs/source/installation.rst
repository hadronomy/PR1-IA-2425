Installation
############

This document provides detailed instructions on how to install and set up the project.

Option 1: Install from Wheel File (Recommended)
************************************************

You can download the wheel file from the `releases page <https://github.com/yourusername/your-repo-name/releases>`_ and install it using `pip`.

.. note::

    This is the recommended method for installing the project as it is the simplest and quickest way to get started.

#. Download the latest `.whl` file from the `releases page <https://github.com/yourusername/your-repo-name/releases>`_.

    Alternatively, you can use the following `curl` command to download the wheel file:

    .. code-block:: sh

      curl -L https://github.com/yourusername/your-repo-name/releases/download/vX.Y.Z/your-wheel-file.whl

#. Install the wheel file using `pip`:

    .. code-block:: sh

        pip install path/to/your-wheel-file.whl

    .. note::

        It is recommended to use `pipx` instead of `pip` to install the wheel file. `pipx` allows you to install and run Python applications in isolated environments.

        You can install `pipx` using the following command:

        .. code-block:: sh

            python3 -m pip install --user pipx
            python3 -m pipx ensurepath

        After installing `pipx`, you can install the wheel file using:

        .. code-block:: sh

            pipx install path/to/your-wheel-file.whl

Option 2: Clone the Repository and Use Poetry
*********************************************

Prerequisites
=============

Before you begin, ensure you have the following installed on your machine:

- `Python 3.12 or higher <https://www.python.org/downloads/release/python-3120/>`_ (only tested in this version)
- `Poetry <https://python-poetry.org/>`_ (for dependency management)

.. note::

    You can install Poetry by following the instructions on the official Poetry website: https://python-poetry.org/docs/#installation

    **TLDR**
    Run the following command:

    .. code-block:: sh

        curl -sSL https://install.python-poetry.org | python3 -

Clone the Repository
====================

First, clone the repository to your local machine:

.. code-block:: sh

    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name

Set Up the Virtual Environment
==============================

Use Poetry to set up a virtual environment and install the dependencies:

.. code-block:: sh

    poetry install

This command will create a virtual environment and install all the required dependencies specified in the ``pyproject.toml`` file.

Activate the Virtual Environment
================================

Activate the virtual environment created by Poetry:

.. code-block:: sh

    poetry shell

This command will activate the virtual environment and allow you to run the CLI commands.

Running the CLI
===============

You can now run the CLI by executing the following command:

.. code-block:: sh

    ia --help

This command will display the help message with all the available commands and options.

Additional Information
======================

For more detailed information, refer to the `README <https://github.com/hadronomy/PR1y2-IA-2425/blob/main/README.md>` file in the root of the repository.