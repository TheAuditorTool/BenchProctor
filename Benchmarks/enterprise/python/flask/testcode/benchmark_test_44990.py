# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest44990():
    xml_value = request.get_data(as_text=True)
    data = ' '.join(str(xml_value).split())
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
