# SPDX-License-Identifier: Apache-2.0
import os
import re
from flask import request, jsonify


def BenchmarkTest53719():
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    os.unlink('/var/app/data/' + str(processed))
    return jsonify({"result": "success"})
