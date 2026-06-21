# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15179():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = '%s' % (graphql_var,)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
