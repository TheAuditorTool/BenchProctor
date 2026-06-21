# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import jsonify
from app_runtime import ssm_client


def BenchmarkTest60661():
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    def normalize(value):
        return value.strip()
    data = normalize(ssm_value)
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
