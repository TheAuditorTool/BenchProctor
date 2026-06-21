# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


def ensure_str(value):
    return str(value)

async def BenchmarkTest30783(request: Request, field: str = Form('')):
    field_value = field
    data = ensure_str(field_value)
    int(str(data))
    return {"updated": True}
