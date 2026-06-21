# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest35375(request: Request):
    user_id = request.query_params.get('id', '')
    data = f'{user_id:.200s}'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    exec(str(processed))
    return {"updated": True}
