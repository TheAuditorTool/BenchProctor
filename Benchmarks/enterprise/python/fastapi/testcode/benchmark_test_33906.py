# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest33906(request: Request):
    origin_value = request.headers.get('origin', '')
    reader = make_reader(origin_value)
    data = reader()
    auth_check('user', data)
    return {"updated": True}
