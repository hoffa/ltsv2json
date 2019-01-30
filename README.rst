ltsv2json
=========

.. image:: https://travis-ci.org/hoffa/ltsv2json.svg?branch=master
   :target: https://travis-ci.org/hoffa/ltsv2json

Reads LTSV from ``stdin`` and prints JSON to ``stdout``.

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
