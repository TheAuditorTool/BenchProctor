# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
import json


async def BenchmarkTest74118(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
