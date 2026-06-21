# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import keyring
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest33601(request: Request):
    secret_value = 'default_setting_value'
    reader = make_reader(secret_value)
    data = reader()
    store_cred = keyring.get_password('app', 'service-account')
    db.connect(host='localhost', user=str(data), password=store_cred)
    return {"updated": True}
