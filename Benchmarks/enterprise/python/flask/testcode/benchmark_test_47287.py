# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest47287():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
