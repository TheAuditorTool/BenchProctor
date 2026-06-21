# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest48889():
    field_value = request.form.get('field', '')
    prefix = ''
    data = prefix + str(field_value)
    requests.get(str(data))
    return jsonify({"result": "success"})
