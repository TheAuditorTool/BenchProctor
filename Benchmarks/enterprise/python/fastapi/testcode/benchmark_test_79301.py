# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest79301(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = '{}'.format(multipart_value)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
