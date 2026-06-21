# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest33260():
    user_id = request.args.get('id', '')
    data = f'{user_id}'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
