# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import keyring
from app_runtime import auth_check


async def BenchmarkTest35856(request: Request):
    secret_value = 'default_config_label'
    data = '%s' % str(secret_value)
    store_cred = keyring.get_password('app', 'service-account')
    auth_check(str(data), store_cred)
    return {"updated": True}
