# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest58999():
    upload_name = request.files['upload'].filename
    data = ' '.join(str(upload_name).split())
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
