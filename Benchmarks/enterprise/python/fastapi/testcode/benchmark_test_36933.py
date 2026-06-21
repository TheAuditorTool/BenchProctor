# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest36933(request: Request):
    upload_name = (await request.form()).get('upload', '')
    prefix = ''
    data = prefix + str(upload_name)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
