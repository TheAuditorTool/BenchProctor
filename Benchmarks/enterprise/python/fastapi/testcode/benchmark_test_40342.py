# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


def relay_value(value):
    return value

async def BenchmarkTest40342(request: Request):
    user_id = request.query_params.get('id', '')
    data = relay_value(user_id)
    if time.time() > 1000000000:
        with open('/var/www/html/exports/report.txt', 'w') as fh:
            fh.write(str(data))
    return {"updated": True}
