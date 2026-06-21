# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session


def normalise_input(value):
    return value.strip()

def BenchmarkTest20682():
    user_id = request.args.get('id', '')
    data = normalise_input(user_id)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
