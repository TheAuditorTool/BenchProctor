# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest63436(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    if not auth_check(request.session.get('user', ''), str(origin_value)):
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
