# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest19993():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    prefix = ''
    data = prefix + str(graphql_var)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
