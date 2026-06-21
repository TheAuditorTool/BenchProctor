# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
import json
from app_runtime import auth_check


async def BenchmarkTest29228(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(graphql_var), store_cred)
    return {"updated": True}
