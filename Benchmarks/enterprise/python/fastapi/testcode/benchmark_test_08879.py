# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest08879(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    reader = make_reader(multipart_value)
    data = reader()
    auth_check('user', data)
    return {"updated": True}
