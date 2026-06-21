# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24450():
    user_id = request.args.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
