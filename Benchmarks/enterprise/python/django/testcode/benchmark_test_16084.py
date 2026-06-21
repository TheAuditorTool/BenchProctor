# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest16084(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = auth_header if auth_header else 'default'
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
