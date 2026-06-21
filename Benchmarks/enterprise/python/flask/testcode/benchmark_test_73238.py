# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
from app_runtime import ssm_client


def to_text(value):
    return str(value).strip()

def BenchmarkTest73238():
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    data = to_text(ssm_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
