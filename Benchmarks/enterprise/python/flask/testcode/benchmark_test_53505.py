# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import jsonify


def BenchmarkTest53505():
    secret_value = 'feature_flag_value'
    data = '%s' % str(secret_value)
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
