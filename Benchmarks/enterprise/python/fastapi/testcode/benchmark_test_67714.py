# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest67714(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = str(auth_header).replace('\x00', '')
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
