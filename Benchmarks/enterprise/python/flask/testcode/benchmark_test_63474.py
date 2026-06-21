# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest63474():
    origin_value = request.headers.get('Origin', '')
    data = normalise_input(origin_value)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
