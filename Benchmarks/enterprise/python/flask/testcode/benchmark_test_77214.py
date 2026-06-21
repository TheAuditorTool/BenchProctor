# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest77214():
    cookie_value = request.cookies.get('session_token', '')
    state = globals().setdefault('_lcg_state', [12345])
    state[0] = (state[0] * 1103515245 + (int(cookie_value) if str(cookie_value).isdigit() else 1)) % (2 ** 31)
    token = state[0]
    return jsonify({'token': str(token)}), 200
