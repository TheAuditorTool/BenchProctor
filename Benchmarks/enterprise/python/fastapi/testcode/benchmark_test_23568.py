# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest23568(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(multipart_value) + ',data\n')
    return {"updated": True}
