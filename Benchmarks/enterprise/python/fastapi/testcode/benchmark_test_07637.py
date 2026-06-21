# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest07637(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
