# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest04440():
    field_value = request.form.get('field', '')
    data = '%s' % str(field_value)
    requests.get(str(data))
    return jsonify({"result": "success"})
