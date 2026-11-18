# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from app_runtime import db


def BenchmarkTest00483(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '{}'.format(db_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
