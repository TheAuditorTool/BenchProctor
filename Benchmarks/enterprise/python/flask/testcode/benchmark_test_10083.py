# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest10083(path_param):
    path_value = path_param
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(path_value), store_cred)
    return jsonify({"result": "success"})
