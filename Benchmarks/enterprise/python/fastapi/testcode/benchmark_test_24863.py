# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest24863(request: Request):
    user_id = request.query_params.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
