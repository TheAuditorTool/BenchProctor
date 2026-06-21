# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from pydantic import BaseModel
from app_runtime import auth_check


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest48420(request: Request, req: UserInput):
    json_value = req.payload
    data = '%s' % (json_value,)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
