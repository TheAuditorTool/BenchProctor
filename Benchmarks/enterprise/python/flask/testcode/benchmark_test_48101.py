# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
from Crypto.Cipher import DES


def BenchmarkTest48101():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
