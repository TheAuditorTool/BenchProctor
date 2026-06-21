# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest40071(request: Request):
    upload_name = (await request.form()).get('upload', '')
    if upload_name:
        data = upload_name
    else:
        data = ''
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
