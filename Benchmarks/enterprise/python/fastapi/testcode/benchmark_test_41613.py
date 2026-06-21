# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest41613(request: Request):
    upload_name = (await request.form()).get('upload', '')
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
