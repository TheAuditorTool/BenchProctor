# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest31060():
    upload_name = request.files['upload'].filename
    data = upload_name if upload_name else 'default'
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
