# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db
from django.contrib.auth.models import User


def BenchmarkTest00118(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = (lambda v: v.strip())(db_value)
    matches = len(User.objects.raw("SELECT * FROM users WHERE name = '" + str(data) + "'"))
    return JsonResponse({'matches': matches}, status=200)
