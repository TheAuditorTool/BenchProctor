# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


async def BenchmarkTest24858(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
