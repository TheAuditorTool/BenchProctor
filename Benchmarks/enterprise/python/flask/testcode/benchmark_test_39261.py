# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import jsonify
import asyncio
from app_runtime import auth_check


def BenchmarkTest39261():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    async def fetch_payload():
        await asyncio.sleep(0)
        return file_value
    data = asyncio.run(fetch_payload())
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
