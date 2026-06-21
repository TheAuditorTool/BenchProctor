# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import keyring
from flask import jsonify
from app_runtime import ssm_client


def BenchmarkTest00153():
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    data, _sep, _rest = str(ssm_value).partition('\x00')
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
