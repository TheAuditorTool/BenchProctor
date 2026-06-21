# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import keyring
from app_runtime import auth_check


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest17412(request: Request):
    secret_value = 'app_display_name'
    reader = make_reader(secret_value)
    data = reader()
    store_cred = keyring.get_password('app', 'service-account')
    auth_check(str(data), store_cred)
    return {"updated": True}
