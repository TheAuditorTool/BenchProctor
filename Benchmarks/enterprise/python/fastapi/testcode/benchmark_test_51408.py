# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


def normalise_input(value):
    return value.strip()

async def BenchmarkTest51408(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = normalise_input(ua_value)
    globals()['counter'] = int(data)
    return {"updated": True}
