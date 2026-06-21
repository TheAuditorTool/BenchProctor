# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import keyring
from app_runtime import auth_check


async def BenchmarkTest12657(request: Request):
    secret_value = 'feature_flag_value'
    data = '%s' % (secret_value,)
    store_cred = keyring.get_password('app', 'service-account')
    auth_check(str(data), store_cred)
    return {"updated": True}
