# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest53149():
    upload_name = request.files['upload'].filename
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(upload_name)):
        return jsonify({'error': 'invalid input'}), 400
    processed = upload_name
    eval(str(processed))
    return jsonify({"result": "success"})
