# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest04433():
    field_value = request.form.get('field', '')
    data = ' '.join(str(field_value).split())
    os.remove(str(data))
    return jsonify({"result": "success"})
