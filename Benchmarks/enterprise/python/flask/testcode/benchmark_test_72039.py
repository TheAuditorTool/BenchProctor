# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest72039():
    upload_name = request.files['upload'].filename
    data = ensure_str(upload_name)
    state = globals().setdefault('_lcg_state', [12345])
    state[0] = (state[0] * 1103515245 + (int(data) if str(data).isdigit() else 1)) % (2 ** 31)
    token = state[0]
    return jsonify({'token': str(token)}), 200
