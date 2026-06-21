# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import asyncio
from app_runtime import auth_check


def BenchmarkTest33434():
    secret_value = ['s3cr3t_key_test_xyz'][0]
    async def fetch_payload():
        await asyncio.sleep(0)
        return secret_value
    data = asyncio.run(fetch_payload())
    auth_check('user', data)
    return jsonify({"result": "success"})
