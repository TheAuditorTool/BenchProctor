# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest09702(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = f'{ua_value}'
    os.system('echo ' + str(data))
    return {"updated": True}
