# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest34737():
    field_value = request.form.get('field', '')
    requests.get(str(field_value))
    return jsonify({"result": "success"})
