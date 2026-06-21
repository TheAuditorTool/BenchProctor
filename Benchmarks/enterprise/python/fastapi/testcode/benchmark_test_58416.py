# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


async def BenchmarkTest58416(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    requests.get(str(data))
    return {"updated": True}
