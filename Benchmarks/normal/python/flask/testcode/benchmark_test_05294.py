# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


def BenchmarkTest05294():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    json.loads(data)
    return jsonify({"result": "success"})
