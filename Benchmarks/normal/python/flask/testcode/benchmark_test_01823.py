# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
from Crypto.Cipher import DES


@dataclass
class FormData:
    payload: str

def BenchmarkTest01823(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
