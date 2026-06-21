# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest18832():
    user_id = request.args.get('id', '')
    data = '%s' % (user_id,)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
