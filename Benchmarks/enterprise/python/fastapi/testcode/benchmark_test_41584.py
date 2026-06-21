# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def relay_value(value):
    return value

async def BenchmarkTest41584(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
