# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest51559():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
