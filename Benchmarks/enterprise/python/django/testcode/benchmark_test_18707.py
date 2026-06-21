# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18707(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = auth_header if auth_header else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
