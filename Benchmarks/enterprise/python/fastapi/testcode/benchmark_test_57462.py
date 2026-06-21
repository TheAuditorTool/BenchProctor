# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest57462(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data, _sep, _rest = str(upload_name).partition('\x00')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
