# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json
import os


async def BenchmarkTest72195(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    yaml.safe_load(data)
    return {"updated": True}
