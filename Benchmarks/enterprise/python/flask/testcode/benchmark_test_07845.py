# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from lxml import etree


def BenchmarkTest07845():
    host_value = request.headers.get('Host', '')
    data = str(host_value).replace('\x00', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
