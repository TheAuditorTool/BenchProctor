# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import jsonify
from app_runtime import db


def BenchmarkTest01690():
    secret_value = 'feature_flag_value'
    data = ' '.join(str(secret_value).split())
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    db.connect(host='localhost', user=str(data), password=store_cred)
    return jsonify({"result": "success"})
