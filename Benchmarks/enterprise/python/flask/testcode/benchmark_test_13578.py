# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest13578():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % (multipart_value,)
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
