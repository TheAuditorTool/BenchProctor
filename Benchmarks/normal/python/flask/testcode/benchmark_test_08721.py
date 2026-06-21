# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import asyncio


def BenchmarkTest08721(path_param):
    path_value = path_param
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = asyncio.run(fetch_payload())
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
