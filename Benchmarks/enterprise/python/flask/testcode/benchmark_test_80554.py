# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest80554():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data, _sep, _rest = str(graphql_var).partition('\x00')
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
