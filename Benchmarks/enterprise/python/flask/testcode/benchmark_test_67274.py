# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import boto3
from flask import request, jsonify


def BenchmarkTest67274():
    upload_name = request.files['upload'].filename
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(upload_name).encode())
    return jsonify({"result": "success"})
