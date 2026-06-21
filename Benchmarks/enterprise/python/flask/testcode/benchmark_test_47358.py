# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest47358():
    ua_value = request.headers.get('User-Agent', '')
    data = normalise_input(ua_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
