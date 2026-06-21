# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest33051():
    multipart_value = request.form.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
