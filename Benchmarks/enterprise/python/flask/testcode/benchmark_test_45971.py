# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from lxml import etree


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest45971():
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
