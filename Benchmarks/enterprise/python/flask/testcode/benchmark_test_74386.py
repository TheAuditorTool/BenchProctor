# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify
import os
import asyncio


def BenchmarkTest74386():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = asyncio.run(fetch_payload())
    if os.environ.get("APP_ENV", "production") != "test":
        yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
