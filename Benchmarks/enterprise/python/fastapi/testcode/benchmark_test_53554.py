# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest53554(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = ' '.join(str(header_value).split())
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    exec(str(processed))
    return {"updated": True}
