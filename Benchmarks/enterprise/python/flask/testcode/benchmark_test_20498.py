# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20498():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
