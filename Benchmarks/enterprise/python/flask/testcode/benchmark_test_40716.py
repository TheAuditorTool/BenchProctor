# SPDX-License-Identifier: Apache-2.0
from flask import request
import json


def BenchmarkTest40716():
    multipart_value = request.form.get('multipart_field', '')
    try:
        data = json.loads(multipart_value).get('value', multipart_value)
    except (json.JSONDecodeError, AttributeError):
        data = multipart_value
    return str(data), 200, {'Content-Type': 'text/html'}
