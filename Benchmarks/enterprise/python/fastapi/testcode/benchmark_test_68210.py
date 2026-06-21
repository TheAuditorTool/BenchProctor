# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest68210(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '{}'.format(auth_header)
    os.remove(str(data))
    return {"updated": True}
