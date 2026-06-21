# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import os
from flask import jsonify
from Crypto.Cipher import DES


@dataclass
class FormData:
    payload: str

def BenchmarkTest62373():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
