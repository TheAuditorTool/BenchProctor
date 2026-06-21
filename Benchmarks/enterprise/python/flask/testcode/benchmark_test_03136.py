# SPDX-License-Identifier: Apache-2.0
import os
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest03136():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
