# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest48352(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name:.200s}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
