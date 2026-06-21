# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest70510():
    raw_body = request.get_data(as_text=True)
    prefix = ''
    data = prefix + str(raw_body)
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
