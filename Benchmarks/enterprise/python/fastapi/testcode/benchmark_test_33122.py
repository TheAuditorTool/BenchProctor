# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest33122(request: Request):
    host_value = request.headers.get('host', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    eval(str(processed))
    return {"updated": True}
