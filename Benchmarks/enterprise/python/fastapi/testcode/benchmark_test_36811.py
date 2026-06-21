# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest36811(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = '{}'.format(multipart_value)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
