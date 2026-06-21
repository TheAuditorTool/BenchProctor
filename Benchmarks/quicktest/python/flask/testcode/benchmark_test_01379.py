# SPDX-License-Identifier: Apache-2.0
import os
import re
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest01379():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
