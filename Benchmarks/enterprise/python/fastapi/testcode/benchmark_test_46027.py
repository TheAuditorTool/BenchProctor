# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest46027(request: Request):
    user_id = request.query_params.get('id', '')
    data = coalesce_blank(user_id)
    def _primary():
        _resp = requests.get(str(data))
        exec(_resp.text)
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
