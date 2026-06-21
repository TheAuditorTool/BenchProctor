# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def relay_value(value):
    return value

async def BenchmarkTest26896(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = relay_value(multipart_value)
    os.remove(str(data))
    return {"updated": True}
