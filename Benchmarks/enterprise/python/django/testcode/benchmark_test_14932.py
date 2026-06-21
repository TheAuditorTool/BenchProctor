# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest14932(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(referer_value),))
    return JsonResponse({"saved": True})
