# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
import defusedxml.ElementTree


def BenchmarkTest42040():
    field_value = request.form.get('field', '')
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
