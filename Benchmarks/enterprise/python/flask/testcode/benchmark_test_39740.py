# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest39740():
    multipart_value = request.form.get('multipart_field', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(multipart_value)):
        return jsonify({'error': 'invalid input'}), 400
    processed = multipart_value
    eval(str(processed))
    return jsonify({"result": "success"})
