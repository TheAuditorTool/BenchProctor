# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
from app_runtime import ssm_client


def BenchmarkTest22553():
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    if ssm_value:
        data = ssm_value
    else:
        data = ''
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
