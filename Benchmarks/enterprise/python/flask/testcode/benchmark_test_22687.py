# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import jsonify
from types import SimpleNamespace
from app_runtime import db, auth_check


def BenchmarkTest22687():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
