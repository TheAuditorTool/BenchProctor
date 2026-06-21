# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
from app_runtime import db, auth_check


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest78426(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    reader = make_reader(db_value)
    data = reader()
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
