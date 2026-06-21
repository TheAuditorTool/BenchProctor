# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
import os


def BenchmarkTest09850():
    auth_header = request.headers.get('Authorization', '')
    try:
        data = json.loads(auth_header).get('value', auth_header)
    except (json.JSONDecodeError, AttributeError):
        data = auth_header
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
