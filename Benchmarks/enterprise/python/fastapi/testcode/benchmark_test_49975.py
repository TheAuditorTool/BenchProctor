# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import json


async def BenchmarkTest49975(request: Request):
    path_value = request.path_params.get('id', '')
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
