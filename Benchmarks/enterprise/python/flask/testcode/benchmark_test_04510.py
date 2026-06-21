# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import asyncio
from app_runtime import auth_check


def BenchmarkTest04510(path_param):
    path_value = path_param
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = asyncio.run(fetch_payload())
    auth_check('user', data)
    return jsonify({"result": "success"})
