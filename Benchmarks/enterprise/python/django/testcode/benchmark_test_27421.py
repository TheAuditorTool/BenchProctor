# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest27421(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    db.users.find({'$where': "this.username == '" + str(auth_header) + "'"})
    return JsonResponse({"saved": True})
