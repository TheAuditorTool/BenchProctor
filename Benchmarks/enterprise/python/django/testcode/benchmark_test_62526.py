# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest62526(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    db.users.find({'$where': "this.username == '" + str(origin_value) + "'"})
    return JsonResponse({"saved": True})
