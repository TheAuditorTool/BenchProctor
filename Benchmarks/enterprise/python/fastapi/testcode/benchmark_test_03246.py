# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest03246(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = (lambda v: v.strip())(upload_name)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
