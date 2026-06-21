# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


def BenchmarkTest13904():
    upload_name = request.files['upload'].filename
    data = ' '.join(str(upload_name).split())
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return jsonify({'validated': str(processed)}), 200
    return jsonify({"result": "success"})
