# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest16116():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body:.200s}'
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
