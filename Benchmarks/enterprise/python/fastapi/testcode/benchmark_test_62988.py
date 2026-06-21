# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import json


async def BenchmarkTest62988(request: Request):
    host_value = request.headers.get('host', '')
    try:
        data = json.loads(host_value).get('value', host_value)
    except (json.JSONDecodeError, AttributeError):
        data = host_value
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
