# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest30165(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    os.unlink('/var/app/data/' + str(data))
    return {"updated": True}
