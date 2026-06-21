# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


def BenchmarkTest13607():
    multipart_value = request.form.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})
