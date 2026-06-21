# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest08302():
    ua_value = request.headers.get('User-Agent', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(ua_value)):
        return jsonify({'error': 'invalid input'}), 400
    processed = ua_value
    db.users.find({'$where': "this.username == '" + str(processed) + "'"})
    return jsonify({"result": "success"})
