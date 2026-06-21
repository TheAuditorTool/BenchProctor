# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.Cipher import DES


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest60216():
    host_value = request.headers.get('Host', '')
    data = RequestPayload(host_value).value
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
