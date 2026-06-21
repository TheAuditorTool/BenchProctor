# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest60260(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '{}'.format(auth_header)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
