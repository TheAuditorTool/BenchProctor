# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest26213(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data, _sep, _rest = str(db_value).partition('\x00')
    class UserProfile:
        def __init__(self):
            self.name = ''
            self.is_admin = False
    parts = str(data).split('=', 1)
    profile = UserProfile()
    if len(parts) == 2:
        setattr(profile, parts[0], parts[1])
    return JsonResponse({'is_admin': profile.is_admin}, status=200)
