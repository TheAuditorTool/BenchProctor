# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


async def BenchmarkTest52857(request: Request):
    secret_value = 'feature_flag_value'
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(secret_value)
    data = collected
    store_cred = os.environ.get('APP_SECRET', '')
    db.connect(host='localhost', user=str(data), password=store_cred)
    return {"updated": True}
