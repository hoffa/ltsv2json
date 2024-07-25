ltsv2json |travis|
==================

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
