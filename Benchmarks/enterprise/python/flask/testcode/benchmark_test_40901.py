# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest40901():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    with open('/var/uploads/' + str(graphql_var), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
