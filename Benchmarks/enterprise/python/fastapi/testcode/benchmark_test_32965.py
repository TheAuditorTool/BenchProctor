# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest32965(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
