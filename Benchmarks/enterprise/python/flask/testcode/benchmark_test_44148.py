# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import keyring
from flask import jsonify
from app_runtime import ssm_client


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest44148():
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    reader = make_reader(ssm_value)
    data = reader()
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
