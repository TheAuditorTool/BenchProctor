# SPDX-License-Identifier: Apache-2.0
import random
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest74246():
    host_value = request.headers.get('Host', '')
    data = FormData(payload=host_value).payload
    state = globals().setdefault('_lcg_state', [12345])
    state[0] = (state[0] * 1103515245 + (int(data) if str(data).isdigit() else 1)) % (2 ** 31)
    token = state[0]
    return jsonify({'token': str(token)}), 200
