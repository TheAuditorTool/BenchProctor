# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import keyring
from app_runtime import db


async def BenchmarkTest61788(request: Request):
    secret_value = 'default_setting_value'
    kind = 'json' if str(secret_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = secret_value
            data = parsed
        case _:
            data = secret_value
    store_cred = keyring.get_password('app', 'service-account')
    db.connect(host='localhost', user=str(data), password=store_cred)
    return {"updated": True}
