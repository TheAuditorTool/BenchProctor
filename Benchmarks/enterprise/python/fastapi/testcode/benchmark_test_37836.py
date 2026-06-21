# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest37836(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data, _sep, _rest = str(upload_name).partition('\x00')
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return {"updated": True}
