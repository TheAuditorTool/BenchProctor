# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from lxml import etree


def BenchmarkTest15384():
    raw_body = request.get_data(as_text=True)
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(raw_body).encode(), _parser)
    return jsonify({"result": "success"})
