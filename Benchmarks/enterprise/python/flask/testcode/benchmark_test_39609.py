# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import asyncio
from app_runtime import auth_check


def BenchmarkTest39609():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    async def fetch_payload():
        await asyncio.sleep(0)
        return yaml_value
    data = asyncio.run(fetch_payload())
    auth_check('user', data)
    return jsonify({"result": "success"})
