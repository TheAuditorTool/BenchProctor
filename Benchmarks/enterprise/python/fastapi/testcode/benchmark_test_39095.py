# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest39095(request: Request, field: str = Form('')):
    field_value = field
    if not str(field_value).isdigit():
        raise ValueError('invalid input: ' + str(field_value))
    return {"updated": True}
