# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from lxml import etree


def BenchmarkTest14945():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(graphql_var).encode(), _parser)
    return jsonify({"result": "success"})
