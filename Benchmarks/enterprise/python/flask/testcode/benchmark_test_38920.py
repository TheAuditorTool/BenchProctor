# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest38920():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
