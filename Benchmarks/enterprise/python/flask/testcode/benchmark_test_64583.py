# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import json


def BenchmarkTest64583():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        data = json.loads(header_value).get('value', header_value)
    except (json.JSONDecodeError, AttributeError):
        data = header_value
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
