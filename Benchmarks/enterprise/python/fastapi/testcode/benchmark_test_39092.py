# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest39092(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ','.join(parts)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
