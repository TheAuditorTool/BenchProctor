# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest69403(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = coalesce_blank(raw_body)
    def _primary():
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
