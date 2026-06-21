# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify
import asyncio


def BenchmarkTest68157():
    raw_body = request.get_data(as_text=True)
    async def fetch_payload():
        await asyncio.sleep(0)
        return raw_body
    data = asyncio.run(fetch_payload())
    yaml.safe_load(data)
    return jsonify({"result": "success"})
