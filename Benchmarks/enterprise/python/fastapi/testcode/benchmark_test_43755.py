# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest43755(request: Request):
    origin_value = request.headers.get('origin', '')
    data = str(origin_value).replace('\x00', '')
    request.session['data'] = str(data)
    return {"updated": True}
