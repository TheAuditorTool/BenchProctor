# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from dataclasses import dataclass
from flask import jsonify
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest68871(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
