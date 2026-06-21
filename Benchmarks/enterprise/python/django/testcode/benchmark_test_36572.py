# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest36572(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ' '.join(str(ua_value).split())
    os.remove(str(data))
    return JsonResponse({"saved": True})
