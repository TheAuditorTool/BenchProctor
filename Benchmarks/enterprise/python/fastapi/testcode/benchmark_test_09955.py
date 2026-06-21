# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest09955(request: Request):
    secret_value = 'default_setting_value'
    reader = make_reader(secret_value)
    data = reader()
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
