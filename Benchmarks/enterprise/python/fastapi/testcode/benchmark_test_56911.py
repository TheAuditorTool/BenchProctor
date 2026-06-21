# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest56911(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % str(host_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
