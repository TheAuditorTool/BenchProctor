# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest61752():
    origin_value = request.headers.get('Origin', '')
    if origin_value not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = origin_value
    os.unlink('/var/app/data/' + str(processed))
    return jsonify({"result": "success"})
