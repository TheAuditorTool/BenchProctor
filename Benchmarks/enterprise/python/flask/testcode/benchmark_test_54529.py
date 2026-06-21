# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest54529():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    prefix = ''
    data = prefix + str(graphql_var)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
