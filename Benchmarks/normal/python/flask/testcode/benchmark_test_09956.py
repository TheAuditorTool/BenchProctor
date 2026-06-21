# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest09956():
    multipart_value = request.form.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
