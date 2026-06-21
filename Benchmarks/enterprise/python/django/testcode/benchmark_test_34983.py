# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest34983(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    reader = make_reader(profile_value)
    data = reader()
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
