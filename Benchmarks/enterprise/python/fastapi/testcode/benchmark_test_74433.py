# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest74433(request: Request):
    upload_name = (await request.form()).get('upload', '')
    reader = make_reader(upload_name)
    data = reader()
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
