# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12324():
    upload_name = request.files['upload'].filename
    data = ' '.join(str(upload_name).split())
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
