# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest07571(request: Request):
    origin_value = request.headers.get('origin', '')
    data = default_blank(origin_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
