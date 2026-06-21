# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import jsonify
import asyncio
from app_runtime import db


def BenchmarkTest14791():
    secret_value = 'default_config_label'
    async def fetch_payload():
        await asyncio.sleep(0)
        return secret_value
    data = asyncio.run(fetch_payload())
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    db.connect(host='localhost', user=str(data), password=store_cred)
    return jsonify({"result": "success"})
