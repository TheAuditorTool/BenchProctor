# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import keyring
from app_runtime import auth_check


async def BenchmarkTest45107(request: Request):
    secret_value = 'default_setting_value'
    data, _sep, _rest = str(secret_value).partition('\x00')
    store_cred = keyring.get_password('app', 'service-account')
    auth_check(str(data), store_cred)
    return {"updated": True}
