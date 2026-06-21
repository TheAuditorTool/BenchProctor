# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import ast
from app_runtime import db


async def BenchmarkTest43105(request: Request):
    secret_value = 'default_config_label'
    try:
        data = str(ast.literal_eval(secret_value))
    except (ValueError, SyntaxError):
        data = secret_value
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    db.connect(host='localhost', user=str(data), password=store_cred)
    return {"updated": True}
