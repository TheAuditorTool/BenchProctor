# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
import ast
from app_runtime import auth_check


async def BenchmarkTest08789(request: Request):
    secret_value = 'feature_flag_value'
    try:
        data = str(ast.literal_eval(secret_value))
    except (ValueError, SyntaxError):
        data = secret_value
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
