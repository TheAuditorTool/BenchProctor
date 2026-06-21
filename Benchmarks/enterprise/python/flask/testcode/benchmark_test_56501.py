# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
from app_runtime import ssm_client


def BenchmarkTest56501():
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    data, _sep, _rest = str(ssm_value).partition('\x00')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
