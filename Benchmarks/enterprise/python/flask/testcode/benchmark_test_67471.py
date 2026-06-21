# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify
import json


def BenchmarkTest67471():
    multipart_value = request.form.get('multipart_field', '')
    try:
        data = json.loads(multipart_value).get('value', multipart_value)
    except (json.JSONDecodeError, AttributeError):
        data = multipart_value
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
