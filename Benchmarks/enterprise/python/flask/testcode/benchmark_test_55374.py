# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import jsonify
import asyncio


def BenchmarkTest55374(path_param):
    path_value = path_param
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = asyncio.run(fetch_payload())
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
