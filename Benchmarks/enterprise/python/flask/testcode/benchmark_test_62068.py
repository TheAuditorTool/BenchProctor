# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import json


def BenchmarkTest62068():
    multipart_value = request.form.get('multipart_field', '')
    try:
        data = json.loads(multipart_value).get('value', multipart_value)
    except (json.JSONDecodeError, AttributeError):
        data = multipart_value
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
