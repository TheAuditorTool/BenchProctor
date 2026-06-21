# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest53661():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % str(multipart_value)
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
