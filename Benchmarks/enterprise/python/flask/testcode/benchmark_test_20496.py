# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest20496():
    multipart_value = request.form.get('multipart_field', '')
    digest = hashlib.sha1(str(multipart_value).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
