# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77839():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = f'{graphql_var:.200s}'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
