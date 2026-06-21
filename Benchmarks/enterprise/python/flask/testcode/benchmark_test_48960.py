# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest48960():
    user_id = request.args.get('id', '')
    data = '%s' % (user_id,)
    if str(data) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
