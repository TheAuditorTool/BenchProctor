# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


def ensure_str(value):
    return str(value)

async def BenchmarkTest47475(request: Request):
    user_id = request.query_params.get('id', '')
    data = ensure_str(user_id)
    globals()['counter'] = int(data)
    return {"updated": True}
