# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
from types import SimpleNamespace
from app_runtime import db, auth_check


def BenchmarkTest55044(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
