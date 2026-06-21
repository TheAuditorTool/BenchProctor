# SPDX-License-Identifier: Apache-2.0
import os
import re
from flask import request, jsonify


def BenchmarkTest37113():
    field_value = request.form.get('field', '')
    data = '%s' % str(field_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
