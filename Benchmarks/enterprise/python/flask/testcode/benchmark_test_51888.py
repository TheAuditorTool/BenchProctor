# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from lxml import etree


request_state: dict[str, str] = {}

def BenchmarkTest51888():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    eval(compile('_parser = etree.XMLParser(resolve_entities=True, no_network=False)\netree.fromstring(str(data).encode(), _parser)', '<sink>', 'exec'))
    return jsonify({"result": "success"})
