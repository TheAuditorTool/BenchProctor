# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest35508(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = normalise_input(db_value)
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
