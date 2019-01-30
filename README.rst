# ltsv2json

[![Build Status](https://travis-ci.org/hoffa/ltsv2json.svg?branch=master)](https://travis-ci.org/hoffa/ltsv2json)

Reads LTSV from `stdin` and prints JSON to `stdout`.

## Installation

```shell
pip install ltsv2json
```

## Usage

```shell
$ printf "world:bar\thello:foo\nworld:turtle" | ltsv2json
{"world":"bar","hello":"foo"}
{"world":"turtle"}
```
