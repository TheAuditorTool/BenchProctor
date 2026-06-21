# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest54042():
    multipart_value = request.form.get('multipart_field', '')
    data = normalise_input(multipart_value)
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
