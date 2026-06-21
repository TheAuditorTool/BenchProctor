# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from lxml import etree


def BenchmarkTest43274():
    host_value = request.headers.get('Host', '')
    data = f'{host_value}'
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
