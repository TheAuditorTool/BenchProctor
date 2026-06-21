# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12872():
    user_id = request.args.get('id', '')
    data = '%s' % (user_id,)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
