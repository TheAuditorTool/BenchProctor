# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest00145(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = coalesce_blank(header_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
