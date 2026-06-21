# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import keyring
from app_runtime import db


async def BenchmarkTest29812(request: Request):
    secret_value = 'feature_flag_value'
    data = '{}'.format(secret_value)
    store_cred = keyring.get_password('app', 'service-account')
    db.connect(host='localhost', user=str(data), password=store_cred)
    return {"updated": True}
