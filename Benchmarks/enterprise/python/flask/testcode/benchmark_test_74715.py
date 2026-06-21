# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from lxml import etree


def BenchmarkTest74715():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = '%s' % (json_value,)
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
