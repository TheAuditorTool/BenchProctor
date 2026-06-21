# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import boto3
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest07171():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
