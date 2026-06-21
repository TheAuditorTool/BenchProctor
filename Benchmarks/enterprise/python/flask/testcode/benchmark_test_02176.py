# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest02176():
    field_value = request.form.get('field', '')
    data = str(field_value).replace('\x00', '')
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
