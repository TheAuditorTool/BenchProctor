# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request


def BenchmarkTest46564():
    field_value = request.form.get('field', '')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(field_value)).read()
    return jsonify({"result": "success"})
