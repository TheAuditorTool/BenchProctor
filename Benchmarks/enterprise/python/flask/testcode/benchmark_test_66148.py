# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest66148():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
