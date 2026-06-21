# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest24868():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    defusedxml.ElementTree.fromstring(str(graphql_var))
    return jsonify({"result": "success"})
