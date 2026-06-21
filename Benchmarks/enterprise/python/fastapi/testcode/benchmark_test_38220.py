# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from app_runtime import db, auth_check


request_state: dict[str, str] = {}

async def BenchmarkTest38220(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
