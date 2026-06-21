# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest79626(request: Request):
    user_id = request.query_params.get('id', '')
    data = f'{user_id}'
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
