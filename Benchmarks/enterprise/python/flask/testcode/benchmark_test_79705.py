# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
import pickle


def BenchmarkTest79705():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    try:
        data = json.loads(graphql_var).get('value', graphql_var)
    except (json.JSONDecodeError, AttributeError):
        data = graphql_var
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
