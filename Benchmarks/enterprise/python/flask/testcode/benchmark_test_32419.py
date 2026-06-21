# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest32419():
    field_value = request.form.get('field', '')
    data = '%s' % (field_value,)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
