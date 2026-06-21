# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
from app_runtime import db


def BenchmarkTest47911(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return JsonResponse({"saved": True})
