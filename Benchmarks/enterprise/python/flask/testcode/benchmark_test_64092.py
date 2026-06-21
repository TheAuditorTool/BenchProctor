# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify
import asyncio


def BenchmarkTest64092():
    origin_value = request.headers.get('Origin', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = asyncio.run(fetch_payload())
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
