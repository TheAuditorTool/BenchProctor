# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import keyring
from app_runtime import db


async def BenchmarkTest56840(request: Request):
    secret_value = 'app_display_name'
    data = '%s' % str(secret_value)
    store_cred = keyring.get_password('app', 'service-account')
    db.connect(host='localhost', user=str(data), password=store_cred)
    return {"updated": True}
