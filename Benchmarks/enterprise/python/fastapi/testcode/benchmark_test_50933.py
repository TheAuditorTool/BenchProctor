# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest50933(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
