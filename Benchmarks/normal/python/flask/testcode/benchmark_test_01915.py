# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from lxml import etree


def BenchmarkTest01915():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
