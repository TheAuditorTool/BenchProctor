# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest03010():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    yaml.safe_load(data)
    return jsonify({"result": "success"})
