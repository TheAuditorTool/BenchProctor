# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import os


def BenchmarkTest28955():
    secret_value = 'feature_flag_value'
    data = f'{secret_value:.200s}'
    Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
