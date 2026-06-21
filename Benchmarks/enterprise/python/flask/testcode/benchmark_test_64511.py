# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest64511():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    os.seteuid(65534)
    return jsonify({"result": "success"})
