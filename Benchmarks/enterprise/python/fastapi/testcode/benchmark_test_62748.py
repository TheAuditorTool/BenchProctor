# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from app_runtime import auth_check


async def BenchmarkTest62748(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(multipart_value), store_cred)
    return {"updated": True}
