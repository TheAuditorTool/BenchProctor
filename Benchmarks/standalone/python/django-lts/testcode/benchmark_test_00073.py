# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db
from django.contrib.auth.models import User


def BenchmarkTest00073(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if db_value:
        data = db_value
    else:
        data = ''
    User.objects.extra(where=["name = '" + str(data) + "'"]).first()
    return JsonResponse({"saved": True})
