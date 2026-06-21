# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest20650(request: Request):
    user_id = request.query_params.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
