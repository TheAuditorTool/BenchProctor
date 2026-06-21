# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from app_runtime import auth_check


async def BenchmarkTest39213(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    kind = 'json' if str(prop_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = prop_value
            data = parsed
        case _:
            data = prop_value
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
