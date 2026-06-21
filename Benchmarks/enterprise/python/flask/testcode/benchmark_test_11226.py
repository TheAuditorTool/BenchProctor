# SPDX-License-Identifier: Apache-2.0
import jwt
import yaml
from flask import jsonify
import asyncio


def BenchmarkTest11226():
    secret_value = 'feature_flag_value'
    async def fetch_payload():
        await asyncio.sleep(0)
        return secret_value
    data = asyncio.run(fetch_payload())
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return jsonify({"result": "success"})
