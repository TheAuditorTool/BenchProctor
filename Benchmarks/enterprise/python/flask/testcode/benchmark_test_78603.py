# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest78603():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    requests.get(str(data))
    return jsonify({"result": "success"})
