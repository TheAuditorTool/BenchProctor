# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest24289():
    user_id = request.args.get('id', '')
    data = coalesce_blank(user_id)
    state = globals().setdefault('_lcg_state', [12345])
    state[0] = (state[0] * 1103515245 + (int(data) if str(data).isdigit() else 1)) % (2 ** 31)
    token = state[0]
    return jsonify({'token': str(token)}), 200
