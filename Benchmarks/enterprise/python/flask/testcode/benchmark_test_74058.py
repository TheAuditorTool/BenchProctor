# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import boto3
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest74058():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    ns = SimpleNamespace(payload=file_value)
    data = getattr(ns, 'payload')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
