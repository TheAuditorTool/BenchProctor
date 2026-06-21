# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest59478(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = f'{auth_header}'
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
