# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest67926():
    user_id = request.args.get('id', '')
    data = normalise_input(user_id)
    return jsonify({'error': 'An internal error occurred'}), 500
