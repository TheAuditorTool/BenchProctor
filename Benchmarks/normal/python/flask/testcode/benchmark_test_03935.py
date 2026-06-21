# SPDX-License-Identifier: Apache-2.0
import hashlib
import json
from flask import request, jsonify


def BenchmarkTest03935():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
