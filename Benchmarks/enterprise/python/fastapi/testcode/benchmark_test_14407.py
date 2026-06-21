# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest14407(request: Request):
    host_value = request.headers.get('host', '')
    data = (lambda v: v.strip())(host_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    request.session['data'] = str(processed)
    return {"updated": True}
