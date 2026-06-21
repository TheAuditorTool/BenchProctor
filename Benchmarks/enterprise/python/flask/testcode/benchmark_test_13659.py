# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest13659():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
