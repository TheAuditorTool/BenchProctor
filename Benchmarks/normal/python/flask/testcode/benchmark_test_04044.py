# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest04044():
    referer_value = request.headers.get('Referer', '')
    data = normalise_input(referer_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
