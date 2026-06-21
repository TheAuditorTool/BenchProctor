# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


def BenchmarkTest33784():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    if re.search('[a-zA-Z0-9_-]+', str(graphql_var)):
        return jsonify({'validated': str(graphql_var)}), 200
    return jsonify({"result": "success"})
