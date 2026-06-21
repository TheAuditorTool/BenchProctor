# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
from flask import redirect
import urllib.parse


def BenchmarkTest28365():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(forwarded_ip)):
        return jsonify({'error': 'invalid input'}), 400
    processed = forwarded_ip
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
