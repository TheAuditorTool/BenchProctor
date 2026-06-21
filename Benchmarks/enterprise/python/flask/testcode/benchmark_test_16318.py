# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16318():
    referer_value = request.headers.get('Referer', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(referer_value)
    data = collected
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
