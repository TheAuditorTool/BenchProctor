# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest36911(request: Request):
    auth_header = request.headers.get('authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    os.system('echo ' + str(data))
    return {"updated": True}
