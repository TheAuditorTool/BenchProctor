# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import asyncio
import defusedxml.ElementTree


def BenchmarkTest57678(path_param):
    path_value = path_param
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = asyncio.run(fetch_payload())
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
