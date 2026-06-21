# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest69725():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = '{}'.format(graphql_var)
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
