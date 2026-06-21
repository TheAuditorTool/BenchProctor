# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
import os


def BenchmarkTest17853():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
