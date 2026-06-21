# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64


async def BenchmarkTest10577(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
