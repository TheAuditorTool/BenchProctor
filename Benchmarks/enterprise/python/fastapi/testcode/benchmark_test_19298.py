# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def to_text(value):
    return str(value).strip()

async def BenchmarkTest19298(request: Request):
    referer_value = request.headers.get('referer', '')
    data = to_text(referer_value)
    def _primary():
        eval(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
