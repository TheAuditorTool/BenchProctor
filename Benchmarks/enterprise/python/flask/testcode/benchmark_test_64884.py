# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
from Crypto.Cipher import DES


def BenchmarkTest64884():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
