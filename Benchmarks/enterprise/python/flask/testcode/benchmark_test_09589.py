# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09589():
    user_id = request.args.get('id', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(user_id))
    return jsonify({"result": "success"})
