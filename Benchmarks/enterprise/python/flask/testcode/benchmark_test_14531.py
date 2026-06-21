# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest14531():
    multipart_value = request.form.get('multipart_field', '')
    entries = os.listdir(str(multipart_value))
    return jsonify({'listing': entries}), 200
