# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest00081():
    multipart_value = request.form.get('multipart_field', '')
    data = '{}'.format(multipart_value)
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
