# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest34387():
    field_value = request.form.get('field', '')
    data = '%s' % str(field_value)
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
