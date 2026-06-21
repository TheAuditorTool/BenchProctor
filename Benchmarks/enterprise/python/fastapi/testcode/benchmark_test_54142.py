# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest54142(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = '%s' % (upload_name,)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
