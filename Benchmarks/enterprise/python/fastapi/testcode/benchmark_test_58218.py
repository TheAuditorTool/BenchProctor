# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest58218(request: Request):
    referer_value = request.headers.get('referer', '')
    data = str(referer_value).replace('\x00', '')
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
