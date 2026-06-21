# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest51333(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name}'
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
