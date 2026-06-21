# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def BenchmarkTest14520():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(data).encode()[:22])
    return jsonify({'length': len(ciphertext)}), 200
