# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest41645():
    field_value = request.form.get('field', '')
    data = ' '.join(str(field_value).split())
    requests.get(str(data))
    return jsonify({"result": "success"})
