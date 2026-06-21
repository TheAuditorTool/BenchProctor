# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest72954(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
