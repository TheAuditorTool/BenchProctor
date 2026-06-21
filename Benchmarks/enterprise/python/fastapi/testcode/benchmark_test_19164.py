# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest19164(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = str(upload_name).replace('\x00', '')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
