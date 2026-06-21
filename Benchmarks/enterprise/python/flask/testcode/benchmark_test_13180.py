# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
from lxml import etree


def BenchmarkTest13180():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
