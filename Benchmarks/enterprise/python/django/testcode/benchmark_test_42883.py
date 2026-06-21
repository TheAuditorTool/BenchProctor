# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest42883(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = ' '.join(str(auth_header).split())
    eval(str(data))
    return JsonResponse({"saved": True})
