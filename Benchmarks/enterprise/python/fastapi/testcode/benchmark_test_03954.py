# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import ast
from app_runtime import auth_check


async def BenchmarkTest03954(request: Request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    try:
        data = str(ast.literal_eval(yaml_value))
    except (ValueError, SyntaxError):
        data = yaml_value
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
