# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import asyncio
import importlib


def BenchmarkTest77533():
    origin_value = request.headers.get('Origin', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = asyncio.run(fetch_payload())
    if os.environ.get("APP_ENV", "production") != "test":
        importlib.import_module(str(data))
    return jsonify({"result": "success"})
