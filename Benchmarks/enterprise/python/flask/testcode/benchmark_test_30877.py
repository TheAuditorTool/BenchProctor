# SPDX-License-Identifier: Apache-2.0
import boto3
from urllib.parse import unquote
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest30877():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
