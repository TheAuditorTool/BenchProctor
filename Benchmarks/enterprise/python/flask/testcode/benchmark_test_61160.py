# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest61160():
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
