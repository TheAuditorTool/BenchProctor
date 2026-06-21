# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest33985(path_param):
    path_value = path_param
    data = coalesce_blank(path_value)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
