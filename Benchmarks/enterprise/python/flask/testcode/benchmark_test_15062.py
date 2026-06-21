# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import boto3
from flask import jsonify


def BenchmarkTest15062():
    secret_value = 'default_config_label'
    data, _sep, _rest = str(secret_value).partition('\x00')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
