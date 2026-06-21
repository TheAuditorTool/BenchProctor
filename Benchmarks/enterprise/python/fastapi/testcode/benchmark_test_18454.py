# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest18454(request: Request):
    auth_header = request.headers.get('authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    os.system('echo ' + str(data))
    return {"updated": True}
