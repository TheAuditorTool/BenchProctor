# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest11172(request: Request):
    user_id = request.query_params.get('id', '')
    data = ' '.join(str(user_id).split())
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    eval(str(processed))
    return {"updated": True}
