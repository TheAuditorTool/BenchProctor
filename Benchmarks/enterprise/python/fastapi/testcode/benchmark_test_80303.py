# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest80303(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = default_blank(multipart_value)
    os.remove(str(data))
    return {"updated": True}
