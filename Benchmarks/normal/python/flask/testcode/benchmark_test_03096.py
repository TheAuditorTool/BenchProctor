# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


def BenchmarkTest03096():
    field_value = request.form.get('field', '')
    if re.search('[a-zA-Z0-9_-]+', str(field_value)):
        return jsonify({'validated': str(field_value)}), 200
    return jsonify({"result": "success"})
