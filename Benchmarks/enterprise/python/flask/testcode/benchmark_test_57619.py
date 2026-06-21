# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest57619():
    xml_value = request.get_data(as_text=True)
    data = coalesce_blank(xml_value)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
