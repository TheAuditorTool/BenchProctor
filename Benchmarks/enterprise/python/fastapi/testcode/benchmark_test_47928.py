# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest47928(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = f'{multipart_value}'
    os.remove(str(data))
    return {"updated": True}
