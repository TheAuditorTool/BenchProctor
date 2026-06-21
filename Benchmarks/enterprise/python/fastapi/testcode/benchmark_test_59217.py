# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest59217(request: Request):
    user_id = request.query_params.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    eval(str(processed))
    return {"updated": True}
