# SPDX-License-Identifier: Apache-2.0
import os
import json
from flask import request, jsonify


def BenchmarkTest05488():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
