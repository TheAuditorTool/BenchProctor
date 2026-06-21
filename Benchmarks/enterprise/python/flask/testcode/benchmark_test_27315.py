# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import boto3
from flask import jsonify
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest27315():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = ensure_str(dotenv_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
