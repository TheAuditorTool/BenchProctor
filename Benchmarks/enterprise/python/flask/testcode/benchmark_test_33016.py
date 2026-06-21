# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
from Crypto.Cipher import DES


@dataclass
class FormData:
    payload: str

def BenchmarkTest33016():
    xml_value = request.get_data(as_text=True)
    data = FormData(payload=xml_value).payload
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
