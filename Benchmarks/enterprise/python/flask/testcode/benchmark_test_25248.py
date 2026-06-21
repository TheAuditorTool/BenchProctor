# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


@dataclass
class FormData:
    payload: str

def BenchmarkTest25248():
    auth_header = request.headers.get('Authorization', '')
    data = FormData(payload=auth_header).payload
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(data).encode()[:22])
    return jsonify({'length': len(ciphertext)}), 200
