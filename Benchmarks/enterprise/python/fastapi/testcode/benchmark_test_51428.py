# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def to_text(value):
    return str(value).strip()

async def BenchmarkTest51428(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    int(str(data))
    return {"updated": True}
