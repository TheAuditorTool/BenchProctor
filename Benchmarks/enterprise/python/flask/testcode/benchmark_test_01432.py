# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest01432():
    field_value = request.form.get('field', '')
    data = relay_value(field_value)
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
