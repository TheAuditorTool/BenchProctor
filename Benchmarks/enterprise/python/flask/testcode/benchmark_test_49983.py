# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest49983():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
