# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest37795():
    raw_body = request.get_data(as_text=True)
    data = '{}'.format(raw_body)
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
