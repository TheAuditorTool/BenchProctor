# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest43702():
    raw_body = request.get_data(as_text=True)
    digest = str(raw_body).encode().hex()
    return jsonify({'digest': str(digest)}), 200
