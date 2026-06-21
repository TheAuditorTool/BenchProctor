# SPDX-License-Identifier: Apache-2.0
import os
import base64
from flask import request, jsonify


def BenchmarkTest79083():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
