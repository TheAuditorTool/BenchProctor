# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import keyring
import ast
from app_runtime import db


async def BenchmarkTest00585(request: Request):
    secret_value = 'feature_flag_value'
    try:
        data = str(ast.literal_eval(secret_value))
    except (ValueError, SyntaxError):
        data = secret_value
    store_cred = keyring.get_password('app', 'service-account')
    db.connect(host='localhost', user=str(data), password=store_cred)
    return {"updated": True}
