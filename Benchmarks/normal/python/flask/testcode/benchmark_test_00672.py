# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify
import asyncio


def BenchmarkTest00672(path_param):
    path_value = path_param
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = asyncio.run(fetch_payload())
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
