# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import ast
from app_runtime import auth_check


async def BenchmarkTest20040(request: Request):
    secret_value = 'default_setting_value'
    try:
        data = str(ast.literal_eval(secret_value))
    except (ValueError, SyntaxError):
        data = secret_value
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    auth_check(str(data), store_cred)
    return {"updated": True}
