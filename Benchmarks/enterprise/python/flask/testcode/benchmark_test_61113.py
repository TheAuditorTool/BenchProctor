# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61113():
    referer_value = request.headers.get('Referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
