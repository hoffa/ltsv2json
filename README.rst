ltsv2json |travis|
==================

.. |travis| image:: https://github.com/hoffa/ltsv2json/workflows/.github/workflows/workflow.yml/badge.svg
   :target: https://github.com/hoffa/ltsv2json/actions

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
