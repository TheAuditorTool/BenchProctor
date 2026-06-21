# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest47154(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    reader = make_reader(cookie_value)
    data = reader()
    auth_check('user', data)
    return {"updated": True}
