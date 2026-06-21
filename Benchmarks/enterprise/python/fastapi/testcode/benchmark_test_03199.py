# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest03199(request: Request, field: str = Form('')):
    field_value = field
    data, _sep, _rest = str(field_value).partition('\x00')
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
