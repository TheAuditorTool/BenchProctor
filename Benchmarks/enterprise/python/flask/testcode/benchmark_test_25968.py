# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
from flask import redirect
import urllib.parse


def BenchmarkTest25968():
    origin_value = request.headers.get('Origin', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
