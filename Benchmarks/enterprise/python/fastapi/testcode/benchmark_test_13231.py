# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest13231(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = coalesce_blank(header_value)
    os.remove(str(data))
    return {"updated": True}
