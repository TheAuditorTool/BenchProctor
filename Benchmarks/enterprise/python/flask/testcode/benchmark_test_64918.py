# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def relay_value(value):
    return value

def BenchmarkTest64918():
    multipart_value = request.form.get('multipart_field', '')
    data = relay_value(multipart_value)
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
