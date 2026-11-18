# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db
from django.contrib.auth.models import User


def BenchmarkTest00607(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data, _sep, _rest = str(profile_value).partition('\x00')
    User.objects.filter(id=data).first()
    return JsonResponse({"saved": True})
