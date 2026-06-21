# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest57446():
    upload_name = request.files['upload'].filename
    data = '%s' % (upload_name,)
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
