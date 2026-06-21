# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest58796(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = str(header_value).replace('\x00', '')
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return JsonResponse({"saved": True})
