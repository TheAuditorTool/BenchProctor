# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import request, jsonify
import asyncio


def BenchmarkTest47532():
    host_value = request.headers.get('Host', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return host_value
    data = asyncio.run(fetch_payload())
    yaml.safe_load(data)
    return jsonify({"result": "success"})
