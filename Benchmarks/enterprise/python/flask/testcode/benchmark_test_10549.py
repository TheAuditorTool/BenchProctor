# SPDX-License-Identifier: Apache-2.0
import os
import re
from flask import request, jsonify


def BenchmarkTest10549():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value}'
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
