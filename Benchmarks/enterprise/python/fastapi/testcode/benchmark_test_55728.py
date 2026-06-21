# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def normalise_input(value):
    return value.strip()

async def BenchmarkTest55728(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = normalise_input(cookie_value)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
