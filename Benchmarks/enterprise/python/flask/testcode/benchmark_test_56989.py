# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest56989():
    multipart_value = request.form.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
