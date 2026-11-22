# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db
from django.contrib.auth.models import User


def BenchmarkTest00054(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data = '{}'.format(profile_value)
    matches = len(User.objects.raw('SELECT * FROM "' + str(data).replace('"', '""') + '"'))
    return JsonResponse({'matches': matches}, status=200)
