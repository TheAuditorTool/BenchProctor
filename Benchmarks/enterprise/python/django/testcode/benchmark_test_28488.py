# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
import base64
from app_runtime import db, auth_check


def BenchmarkTest28488(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
