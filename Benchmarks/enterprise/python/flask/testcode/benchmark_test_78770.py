# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest78770():
    field_value = request.form.get('field', '')
    random.seed(int(field_value) if str(field_value).isdigit() else 99)
    token = random.randint(0, 99)
    return jsonify({'token': str(token)}), 200
