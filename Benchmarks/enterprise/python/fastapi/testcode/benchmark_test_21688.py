# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import os


async def BenchmarkTest21688(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
