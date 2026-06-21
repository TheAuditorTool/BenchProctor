# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest15591():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    digest = hashlib.sha256(str(graphql_var).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return jsonify({"result": "success"})
