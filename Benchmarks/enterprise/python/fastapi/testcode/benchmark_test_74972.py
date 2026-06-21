# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest74972(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
