# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import jsonify
import asyncio


def BenchmarkTest11024(path_param):
    path_value = path_param
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = asyncio.run(fetch_payload())
    yaml.safe_load(data)
    return jsonify({"result": "success"})
