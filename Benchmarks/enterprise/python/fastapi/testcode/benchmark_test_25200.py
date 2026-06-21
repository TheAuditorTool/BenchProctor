# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest25200(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    with open('/var/uploads/' + str(multipart_value), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
