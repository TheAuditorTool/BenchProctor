# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import os


async def BenchmarkTest13071(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    yaml.safe_load(data)
    return {"updated": True}
