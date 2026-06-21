# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def BenchmarkTest71606():
    field_value = request.form.get('field', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(field_value)}, verify=False)
    return jsonify({"result": "success"})
