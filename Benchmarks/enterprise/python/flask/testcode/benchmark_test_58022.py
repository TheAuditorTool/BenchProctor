# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import boto3
from urllib.parse import unquote
from flask import request, jsonify
import os
import time


def BenchmarkTest58022():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    key_expires_at = 4102444800
    active_key = store_cred if key_expires_at > int(time.time()) else os.environ['DATA_ENC_KEY_CURRENT']
    Fernet(active_key.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
