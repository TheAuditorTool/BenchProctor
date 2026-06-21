# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import boto3
from flask import jsonify
from app_runtime import ssm_client


def BenchmarkTest16186():
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    data = f'{ssm_value}'
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
