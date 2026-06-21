# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import os


def BenchmarkTest59006(path_param):
    path_value = path_param
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(path_value).encode())
    return jsonify({'length': len(ciphertext)}), 200
