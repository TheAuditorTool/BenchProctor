# SPDX-License-Identifier: Apache-2.0
import random
from flask import jsonify


def BenchmarkTest03752(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    state = globals().setdefault('_lcg_state', [12345])
    state[0] = (state[0] * 1103515245 + (int(data) if str(data).isdigit() else 1)) % (2 ** 31)
    token = state[0]
    return jsonify({'token': str(token)}), 200
