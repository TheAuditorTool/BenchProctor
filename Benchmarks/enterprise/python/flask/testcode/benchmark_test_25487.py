# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from Crypto.Cipher import DES


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest25487():
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
