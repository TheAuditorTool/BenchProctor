# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import urllib.request


async def BenchmarkTest58875(request: Request, field: str = Form('')):
    field_value = field
    parts = []
    for token in str(field_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
