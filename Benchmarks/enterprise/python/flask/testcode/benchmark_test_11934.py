# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11934():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
