# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest52624():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    if str(data) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
