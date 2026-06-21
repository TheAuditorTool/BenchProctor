# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest56930(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    os.remove(str(data))
    return {"updated": True}
