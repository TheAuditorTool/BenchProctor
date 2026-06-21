# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest20231():
    upload_name = request.files['upload'].filename
    state = globals().setdefault('_lcg_state', [12345])
    state[0] = (state[0] * 1103515245 + (int(upload_name) if str(upload_name).isdigit() else 1)) % (2 ** 31)
    token = state[0]
    return jsonify({'token': str(token)}), 200
