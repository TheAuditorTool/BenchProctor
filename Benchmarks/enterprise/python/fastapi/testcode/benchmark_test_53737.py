# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest53737(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = coalesce_blank(header_value)
    def _primary():
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
