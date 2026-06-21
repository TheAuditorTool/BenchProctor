# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db, User


def BenchmarkTest08717(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data, _sep, _rest = str(db_value).partition('\x00')
    db.session.query(User).filter(User.id == data).all()
    return JsonResponse({"saved": True})
