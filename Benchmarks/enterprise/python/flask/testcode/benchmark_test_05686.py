# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
from Crypto.Cipher import DES


def BenchmarkTest05686():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
