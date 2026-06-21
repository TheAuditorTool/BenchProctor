# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18667(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = f'{auth_header}'
    int(str(data))
    return JsonResponse({"saved": True})
