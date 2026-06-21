# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import keyring
from app_runtime import db


async def BenchmarkTest07894(request: Request):
    secret_value = 'default_config_label'
    data = (lambda v: v.strip())(secret_value)
    store_cred = keyring.get_password('app', 'service-account')
    db.connect(host='localhost', user=str(data), password=store_cred)
    return {"updated": True}
