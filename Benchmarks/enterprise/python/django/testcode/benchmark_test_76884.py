# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest76884(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '%s' % (referer_value,)
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return JsonResponse({"saved": True})
