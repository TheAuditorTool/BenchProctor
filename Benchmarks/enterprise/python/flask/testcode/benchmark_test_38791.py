# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import asyncio


def BenchmarkTest38791():
    host_value = request.headers.get('Host', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return host_value
    data = asyncio.run(fetch_payload())
    if os.environ.get("APP_ENV", "production") != "test":
        os.system('echo ' + str(data))
    return jsonify({"result": "success"})
