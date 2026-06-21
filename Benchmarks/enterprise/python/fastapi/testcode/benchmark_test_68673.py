# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest68673(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value}'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
