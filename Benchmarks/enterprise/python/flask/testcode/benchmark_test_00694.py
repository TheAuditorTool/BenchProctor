# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00694():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
