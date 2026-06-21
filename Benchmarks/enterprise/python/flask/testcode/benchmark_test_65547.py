# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest65547():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    values = str(data).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
