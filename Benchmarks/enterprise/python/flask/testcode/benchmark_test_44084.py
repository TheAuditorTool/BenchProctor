# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest44084():
    user_id = request.args.get('id', '')
    data = '%s' % str(user_id)
    values = str(data).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
