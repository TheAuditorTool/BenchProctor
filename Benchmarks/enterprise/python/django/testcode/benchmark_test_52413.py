# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest52413(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = f'{ua_value:.200s}'
    eval(str(data))
    return JsonResponse({"saved": True})
