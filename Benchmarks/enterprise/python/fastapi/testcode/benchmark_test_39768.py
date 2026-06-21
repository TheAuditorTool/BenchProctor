# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest39768(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = (lambda v: v.strip())(upload_name)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
