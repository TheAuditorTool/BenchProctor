# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest40235(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value:.200s}'
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
