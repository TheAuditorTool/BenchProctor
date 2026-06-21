# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from lxml import etree


def BenchmarkTest62851():
    env_value = os.environ.get('USER_INPUT', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(env_value).encode(), _parser)
    return jsonify({"result": "success"})
