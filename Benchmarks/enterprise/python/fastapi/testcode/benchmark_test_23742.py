# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
import ast
from app_runtime import auth_check


async def BenchmarkTest23742(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    try:
        data = str(ast.literal_eval(file_value))
    except (ValueError, SyntaxError):
        data = file_value
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
