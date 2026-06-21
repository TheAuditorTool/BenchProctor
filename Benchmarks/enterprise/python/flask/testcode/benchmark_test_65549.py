# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def BenchmarkTest65549():
    upload_name = request.files['upload'].filename
    try:
        data = json.loads(upload_name).get('value', upload_name)
    except (json.JSONDecodeError, AttributeError):
        data = upload_name
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(data).encode()[:22])
    return jsonify({'length': len(ciphertext)}), 200
