# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest45950(request: Request):
    path_value = request.path_params.get('id', '')
    prefix = ''
    data = prefix + str(path_value)
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
