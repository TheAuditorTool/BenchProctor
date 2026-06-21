# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest79603():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    requests.get(str(data))
    return jsonify({"result": "success"})
