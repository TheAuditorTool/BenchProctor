# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import jsonify
import os
import asyncio


def BenchmarkTest40604(path_param):
    path_value = path_param
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = asyncio.run(fetch_payload())
    if os.environ.get("APP_ENV", "production") != "test":
        subprocess.Popen('echo ' + str(data), shell=True).wait()
    return jsonify({"result": "success"})
