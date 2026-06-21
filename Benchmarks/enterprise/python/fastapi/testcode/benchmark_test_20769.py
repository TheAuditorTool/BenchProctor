# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest20769(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '{}'.format(auth_header)
    os.system('echo ' + str(data))
    return {"updated": True}
