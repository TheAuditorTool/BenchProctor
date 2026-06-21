# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest02229():
    field_value = request.form.get('field', '')
    data = f'{field_value}'
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
