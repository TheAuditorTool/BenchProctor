# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest20023(request: Request):
    host_value = request.headers.get('host', '')
    data = coalesce_blank(host_value)
    def _primary():
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
