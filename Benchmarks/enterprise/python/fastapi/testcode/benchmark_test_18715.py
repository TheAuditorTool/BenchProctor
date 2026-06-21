# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import os


async def BenchmarkTest18715(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
