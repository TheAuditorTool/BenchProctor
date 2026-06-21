# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

async def BenchmarkTest78649(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
