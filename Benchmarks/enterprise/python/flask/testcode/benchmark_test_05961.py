# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
import os


def BenchmarkTest05961():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
