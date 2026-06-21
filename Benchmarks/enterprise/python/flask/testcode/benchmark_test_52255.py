# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import boto3
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest52255():
    secret_value = 'default_setting_value'
    reader = make_reader(secret_value)
    data = reader()
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
