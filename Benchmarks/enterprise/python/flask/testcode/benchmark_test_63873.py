# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import redirect
import urllib.parse


def BenchmarkTest63873():
    header_value = request.headers.get('X-Custom-Header', '')
    if header_value not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = header_value
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
