# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import boto3
from flask import jsonify


def BenchmarkTest30029():
    secret_value = 'app_display_name'
    data = '%s' % (secret_value,)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
