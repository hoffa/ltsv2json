ltsv2json
=========

.. image:: https://img.shields.io/pypi/dm/ltsv2json
   :alt: PyPI - Downloads

.. image:: https://img.shields.io/pypi/v/ltsv2json
   :alt: PyPI - Version

Reads LTSV from stdin and prints JSON to stdout.

Installation
------------

::

  pip install ltsv2json

Usage
-----

::

  $ printf "world:bar\thello:foo\nworld:turtle" | ltsv2json
  {"world":"bar","hello":"foo"}
  {"world":"turtle"}
