# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.Cipher import DES


def BenchmarkTest02082():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value:.200s}'
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
