# SPDX-License-Identifier: Apache-2.0
import hashlib
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest45738():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
