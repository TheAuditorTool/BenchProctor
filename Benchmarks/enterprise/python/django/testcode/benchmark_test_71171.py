# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest71171(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    processed = 'true' if str(forwarded_ip).lower() in ('true', '1', 'yes', 'on') else 'false'
    db.users.find({'$where': "this.username == '" + str(processed) + "'"})
    return JsonResponse({"saved": True})
