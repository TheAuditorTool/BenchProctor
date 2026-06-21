# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest34426(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = (lambda v: v.strip())(auth_header)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    exec(str(processed))
    return {"updated": True}
