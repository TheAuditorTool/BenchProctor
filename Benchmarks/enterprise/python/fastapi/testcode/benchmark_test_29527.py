# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest29527(request: Request):
    ua_value = request.headers.get('user-agent', '')
    def normalize(value):
        return value.strip()
    data = normalize(ua_value)
    os.system('echo ' + str(data))
    return {"updated": True}
