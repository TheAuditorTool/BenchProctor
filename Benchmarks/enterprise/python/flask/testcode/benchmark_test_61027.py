# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import asyncio
import defusedxml.ElementTree


def BenchmarkTest61027():
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = asyncio.run(fetch_payload())
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
