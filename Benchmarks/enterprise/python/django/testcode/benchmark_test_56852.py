# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56852(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = f'{auth_header:.200s}'
    eval(str(data))
    return JsonResponse({"saved": True})
