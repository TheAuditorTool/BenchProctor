# SPDX-License-Identifier: Apache-2.0
import re
from urllib.parse import unquote
from flask import request, jsonify
from flask import redirect
import urllib.parse


def BenchmarkTest48467():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
