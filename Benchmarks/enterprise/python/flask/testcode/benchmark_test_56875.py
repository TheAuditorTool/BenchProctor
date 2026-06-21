# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest56875():
    raw_body = request.get_data(as_text=True)
    data = ' '.join(str(raw_body).split())
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
