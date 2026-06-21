# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest15184(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = f'{auth_header}'
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
