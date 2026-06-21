# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest08687():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
