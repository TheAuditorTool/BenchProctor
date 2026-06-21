# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
from lxml import etree


def BenchmarkTest76002():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
