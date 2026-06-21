# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest46333():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
