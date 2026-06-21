# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest22188():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
