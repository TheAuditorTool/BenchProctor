# SPDX-License-Identifier: Apache-2.0
import os
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest53696():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
