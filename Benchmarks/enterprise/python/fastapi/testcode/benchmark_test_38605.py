# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest38605(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = (lambda v: v.strip())(xml_value)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
