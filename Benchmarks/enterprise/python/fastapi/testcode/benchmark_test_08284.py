# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest08284(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
