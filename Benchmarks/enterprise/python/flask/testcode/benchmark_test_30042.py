# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import asyncio


def BenchmarkTest30042():
    auth_header = request.headers.get('Authorization', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = asyncio.run(fetch_payload())
    if os.environ.get("APP_ENV", "production") != "test":
        os.system('echo ' + str(data))
    return jsonify({"result": "success"})
