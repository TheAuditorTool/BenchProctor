# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from lxml import etree


def BenchmarkTest07055():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(json_value).encode(), _parser)
    return jsonify({"result": "success"})
