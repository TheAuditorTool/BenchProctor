# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from lxml import etree


def BenchmarkTest07276():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
