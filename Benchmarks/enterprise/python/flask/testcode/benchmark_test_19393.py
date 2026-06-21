# SPDX-License-Identifier: Apache-2.0
import subprocess
import os
from flask import jsonify
import asyncio


def coalesce_blank(value):
    return value or ''

def BenchmarkTest19393():
    env_value = os.environ.get('USER_INPUT', '')
    data = coalesce_blank(env_value)
    async def _evasion_task():
        subprocess.Popen('echo ' + str(data), shell=True).wait()
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
