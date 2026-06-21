# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest04908(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data = normalise_input(profile_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
