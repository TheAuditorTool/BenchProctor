# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest73200(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
