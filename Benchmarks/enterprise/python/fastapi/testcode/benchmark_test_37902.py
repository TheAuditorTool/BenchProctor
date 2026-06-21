# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json
import os


async def BenchmarkTest37902(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    yaml.safe_load(data)
    return {"updated": True}
