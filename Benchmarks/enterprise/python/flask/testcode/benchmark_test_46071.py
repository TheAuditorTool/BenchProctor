# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
from app_runtime import ssm_client


def BenchmarkTest46071():
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    data = str(ssm_value).replace('\x00', '')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
