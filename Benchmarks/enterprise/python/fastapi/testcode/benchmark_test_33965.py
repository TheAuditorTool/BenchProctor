# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest33965(request: Request):
    referer_value = request.headers.get('referer', '')
    data = (lambda v: v.strip())(referer_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    exec(str(processed))
    return {"updated": True}
